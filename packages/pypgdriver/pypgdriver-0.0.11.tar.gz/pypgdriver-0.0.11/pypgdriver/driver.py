import asyncio
import os
import re
import logging
import sys
from functools import partial
from typing import (
    Iterator, Optional, Tuple, Union, Awaitable, TypeVar
)

import psycopg2 as psql
import psycopg2.extensions as psqlex
from psycopg2 import connect
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import DictCursor, execute_values
from tornado.concurrent import Future, chain_future, future_set_exc_info
from tornado.ioloop import IOLoop
from multiprocessing import cpu_count
from concurrent.futures.thread import ThreadPoolExecutor

from ._querydata import _QeryData
from .querydata import QueryData
from .querytype import QueryType

_T = TypeVar('_T')

logger = logging.getLogger(__name__)


class PostgreDriver:

    def get_loop(self):
        # return asyncio.get_event_loop()
        return IOLoop.current()

    def __init__(self, **kwargs: dict):
        """
        Parameters
        ----------------------------------------------------------------
            host ホスト名 環境変数 postgreHost
            dbname データベース名 postgreDBname
            user ユーザー名 環境変数 postgreUser
            password パスワード 環境変数 postgrePass
        ----------------------------------------------------------------
        """
        self.cpu_count = cpu_count() * 5
        self._executer = ThreadPoolExecutor(max_workers=self.cpu_count)
        self.Connection = kwargs.get("conn", None)
        if not self.Connection:
            POSTGRE = "postgre"
            self.host = os.environ.get(POSTGRE + "Host", kwargs.get("host"))
            self.dbname = os.environ.get(
                POSTGRE + "DBname", kwargs.get("dbname"))
            self.user = os.environ.get(POSTGRE + "User", kwargs.get("user"))
            self.password = os.environ.get(
                POSTGRE + "Password", kwargs.get("password"))
            port = os.environ.get(POSTGRE + "Port", kwargs.get('port', 5432))
            self.port = int(port)
        self.loop: "IOLoop" = kwargs.get('loop', self.get_loop())
        self.fileno = None

    def connect_async(self) -> "Future[_T]":
        future = Future()

        def _connection(fut: "Future[_T]"):
            exc = self.is_future_exception(fut)
            if exc:
                logger.exception(exc)
                future.set_result(None)
                # future.set_exception(exc)
                return
            self.Connection = fut.result()
            future.set_result(self.Connection)

        future_con = self._executer.submit(partial(connect,
                                                   host=self.host,
                                                   database=self.dbname,
                                                   user=self.user,
                                                   password=self.password,
                                                   port=self.port))
        self.loop.add_future(future_con, _connection)
        return future

    def connect_async2(self) -> "Future[_T]":
        future = Future()

        def _connection(fut: "Future[_T]"):
            exc = self.is_future_exception(fut)
            if exc:
                future.set_exception(exc)
                return
            self.Connection = fut.result()
            future.set_result(self.Connection)

        try:
            self.Connection = psql.connect(host=self.host,
                                           database=self.dbname,
                                           user=self.user,
                                           password=self.password,
                                           port=self.port, async_=1)
        except psql.Error:
            self.Connection = None
            future_set_exc_info(future, sys.exc_info())
            return future
        self.fileno = self.Connection.fileno()
        callback = partial(self._io_callback, future, self)
        self.loop.add_handler(self.fileno, callback, IOLoop.WRITE)
        self.loop.add_future(future, self._close_on_faile)
        return future

    def _close_on_faile(self, future: "Future[_T]"):
        if future.exception():
            self.Connection = None

    def _io_callback(self, future, result, fd=None, event=None):
        try:
            state = self.Connection.poll()
        except (psql.Warning, psql.Error) as error:
            self.loop.remove_handler(self.fileno)
            future_set_exc_info(future, sys.exc_info())
        else:
            try:
                if state == psqlex.POLL_OK:
                    self.loop.remove_handler(self.fileno)
                    future.set_result(result)
                elif state == psqlex.POLL_READ:
                    self.loop.update_handler(self.fileno, IOLoop.READ)
                elif state == psqlex.POLL_WRITE:
                    self.loop.update_handler(self.fileno, IOLoop.WRITE)
                else:
                    future.set_exception(psql.OperationalError(
                        "poll() returned %s" % state))
            except IOError:
                future.set_exception(
                    psql.OperationalError("IOError on socket"))

    def connect(self):
        if not self.Connection:
            self.Connection = connect(
                host=self.host, database=self.dbname, user=self.user, password=self.password, port=self.port)

    def _query(self, kwargs: dict) -> Union[_QeryData, QueryData, int, None]:
        sql = kwargs.pop('sql')
        data = kwargs.pop('data')

        def query_type():
            _sql = sql[:6]
            if re.search(r"select", _sql, re.IGNORECASE):
                return QueryType.select
            elif re.search(r'update', _sql, re.IGNORECASE):
                return QueryType.update
            elif re.search(r'delete', _sql, re.IGNORECASE):
                return QueryType.delete
            elif re.search(r'insert', _sql, re.IGNORECASE):
                return QueryType.insert
            else:
                return QueryType.etc

        self.type = query_type()
        if self.Connection:
            cur = self.Connection.cursor(cursor_factory=DictCursor)
            cur.execute(sql, data)
            return cur
        return None

    def _query_async(self, kwargs: dict):
        sql = kwargs.pop('sql')
        data = kwargs.pop('data')

        def query_type():
            _sql = sql[:6]
            if re.search(r"select", _sql, re.IGNORECASE):
                return QueryType.select
            elif re.search(r'update', _sql, re.IGNORECASE):
                return QueryType.update
            elif re.search(r'delete', _sql, re.IGNORECASE):
                return QueryType.delete
            elif re.search(r'insert', _sql, re.IGNORECASE):
                return QueryType.insert
            else:
                return QueryType.etc

        self.type = query_type()
        cur = self.Connection.cursor(cursor_factory=DictCursor)
        cur.execute(sql, data)
        future = Future()
        callback = partial(self._io_callback, future, cur)
        self.loop.add_handler(self.fileno, callback, IOLoop.WRITE)
        return future

    def execute_async(self, sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> "Future[_T]":
        """
        Return
        --------------------------------------------------------

        * １件取得時  ： _QueryData or None

        * 複数件取得  ： QueryData

        * 登・更・削  ： int, Connection Object
        """
        future = Future()
        future_con: "Future[_T]" = None
        if not isinstance(sql, str):
            sql = str(sql)
        kwargs['sql'] = sql
        kwargs['data'] = data
        if not self.Connection:
            future_con = self.connect_async()

        def _execute(fut: "Future[_T]"):
            exc = self.is_future_exception(fut)
            if exc:
                logger.exception(exc)
                future.set_result(None)
                # future.set_exception(exc)
                return
            result = fut.result()

            def _fetch_all_result(_fut: "Future[_T]"):
                exc = self.is_future_exception(_fut)
                if exc:
                    logger.exception(exc)
                    future.set_result(None)
                    return
                cur_data = _fut.result()
                if cur_data:
                    future.set_result(QueryData(cur_data, result.rowcount))
                else:
                    future.set_result(QueryData([], 0))
                self.Connection.close()

            def _fetch_one_result(_fut: "Future[_T]"):
                exc = self.is_future_exception(_fut)
                if exc:
                    logger.exception(exc)
                    future.set_result(None)
                    return
                cur_data = _fut.result()
                if cur_data:
                    future.set_result(_QeryData(cur_data))
                else:
                    future.set_result(_QeryData({}))

            if result:
                # 正しくConnectionが張られている時
                if self.type == QueryType.select:
                    if kwargs.get('cnt', 0) == 1:
                        future_cur = self._executer.submit(result.fetchone)
                        self.loop.add_future(future_cur, _fetch_one_result)
                    else:
                        future_cur = self._executer.submit(result.fetchall)
                        self.loop.add_future(future_cur, _fetch_all_result)
                else:
                    future.set_result(result.rowcount)
            else:
                if self.type == QueryType.select:
                    if kwargs.get('cnt', 0) == 1:
                        future.set_result(_QeryData({}))
                    else:
                        future.set_result(QueryData([], 0))
                else:
                    future.set_result(0)

        def add_future(fut: "Future[_T]"):
            future_th = self._executer.submit(self._query, kwargs)
            self.loop.add_future(future_th, _execute)

        if future_con:
            self.loop.add_future(future_con, add_future)
        else:
            future_th = self._executer.submit(self._query, kwargs)
            self.loop.add_future(future_th, _execute)
        return future

    def is_future_exception(self, future: 'Future[_T]'):
        return future.exception()

    def execute_async2(self, sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> "Future[_T]":
        """
        Return
        --------------------------------------------------------

        * １件取得時  ： _QueryData or None

        * 複数件取得  ： QueryData

        * 登・更・削  ： int, Connection Object
        """
        future = Future()
        future_con: "Future[_T]" = None
        if not isinstance(sql, str):
            sql = str(sql)
        kwargs['sql'] = sql
        kwargs['data'] = data
        if not self.Connection:
            future_con = self.connect_async()

        def _execute(fut: "Future[_T]"):
            exc = self.is_future_exception(fut)
            if exc:
                future.set_exception(exc)
                return
            result = fut.result()

            def _fetch_all_result(_fut: "Future[_T]"):
                exc = self.is_future_exception(_fut)
                if exc:
                    future.set_exception(exc)
                    return
                cur_data = _fut.result()
                if cur_data:
                    future.set_result(QueryData(cur_data, result.rowcount))
                else:
                    future.set_result(None)

            def _fetch_one_result(_fut: "Future[_T]"):
                exc = self.is_future_exception(_fut)
                if exc:
                    future.set_exception(exc)
                    return

                cur_data = _fut.result()
                if cur_data:
                    future.set_result(_QeryData(cur_data))
                else:
                    future.set_result(None)
            if self.type == QueryType.select:
                if kwargs.get('cnt', 0) == 1:
                    future_cur = self._executer.submit(result.fetchone)
                    self.loop.add_future(future_cur, _fetch_one_result)
                else:
                    future_cur = self._executer.submit(result.fetchall)
                    self.loop.add_future(future_cur, _fetch_all_result)
            else:
                future.set_result(result.rowcount)

        def add_future(fut: "Future[_T]"):
            future_th = self._query_async(kwargs)
            self.loop.add_future(future_th, _execute)

        if future_con:
            self.loop.add_future(future_con, add_future)
        else:
            future_th = self._executer.submit(self._query, kwargs)
            self.loop.add_future(future_th, _execute)
        return future

    def execute(self, sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> Awaitable[_T]:
        """
        Return
        --------------------------------------------------------

        * １件取得時  ： _QueryData or None

        * 複数件取得  ： QueryData

        * 登・更・削  ： int, Connection Object
        """
        if not isinstance(sql, str):
            sql = str(sql)
        kwargs['sql'] = sql
        kwargs['data'] = data
        result = self._query(kwargs)
        if self.type == QueryType.select:
            if kwargs.get('cnt', 0) == 1:
                return _QeryData(result.fetchone())
            else:
                return QueryData(result.fetchall(), result.rowcount)
        else:
            return result.rowcount

    def _copy_from(self, kwargs):
        try:
            f = kwargs['f']
            tableName = kwargs['tableName']
            sep = kwargs['sep']
            null = kwargs['null']
            columns = kwargs['columns']
            cur = self.Connection.cursor()
            cur.copy_from(f, tableName, sep=sep, null=null, columns=columns)
            return True, None
        except psql.Error as e:
            return False, e.pgerror

    def _get_ioString(self, body: Iterator[Iterator[str]]):
        import io
        data = '\n'.join(['\t'.join(d) for d in body])
        return io.StringIO('\n'.join(data), newline="\n")

    def copy_from_async(self, body, tableName, sep="\t", null='\\N', columns=None):
        f = self._get_ioString(body)
        kwargs = {
            'f': f,
            'tableName': tableName,
            'sep': sep,
            'null': null,
            'columns': columns
        }
        future = self.loop.run_in_executor(
            self._executer, self._copy_from, kwargs)
        return future

    def copy_from(self, body, tableName, sep="\t", null='\\N', columns=None):
        f = self._get_ioString(body)
        kwargs = {
            'f': f,
            'tableName': tableName,
            'sep': sep,
            'null': null,
            'columns': columns
        }
        data, e = self._copy_from(kwargs)
        if data:
            return data
        else:
            raise Exception(e)

    def bulk_insert(self, tableName, datas: Iterator[Iterator[object]]):
        cur = self.Connection.cursor()
        sql = 'insert into {tableName} values %s'.format(tableName=tableName)
        return execute_values(cur, sql, datas)
        # return True

    def _bulk_insert(self, kwargs):
        cur = self.Connection.cursor()
        sql = kwargs['sql']
        datas = kwargs['datas']
        return execute_values(cur, sql, datas)

    def bulk_insert_async(self, tableName, datas: Iterator[Iterator[object]]):
        try:
            sql = 'insert into {tableName} values %s'.format(
                tableName=tableName)
            k = {
                'sql': sql,
                'datas': datas
            }
            future = self.loop.run_in_executor(
                self._executer, self._bulk_insert, k)
            return future
        except Exception as e:
            raise e

    @staticmethod
    def query(sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> Union[_QeryData, QueryData, Tuple[_T, 'PostgreDriver'], None]:
        posgre: 'PostgreDriver' = PostgreDriver()
        posgre.connect()
        data = posgre.execute(sql, data, **kwargs)
        if posgre.type != QueryType.select:
            return data, posgre
        else:
            if kwargs.get('returnConnection', False):
                return data, posgre
        del posgre
        return data

    @staticmethod
    async def query_async(sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> Union[_QeryData, QueryData, Tuple[_T, 'PostgreDriver'], None]:
        """
        Return
        --------------------------------------------------------
            １件取得時  ： _QueryData or None
            複数件取得  ： QueryData
            登・更・削  ： int,Connection Object
        """
        posgre: 'PostgreDriver' = PostgreDriver()
        data = await posgre.execute_async(sql, data, **kwargs)
        if posgre.type != QueryType.select:
            return data, posgre
        else:
            if kwargs.get('return_connection', False):
                return data, posgre
        del posgre
        return data

    def commit(self):
        self.Connection.commit()

    def rollback(self):
        self.Connection.rollback()

    def _close(self):
        try:
            self.Connection.close()
        except:
            pass
        try:
            if self._executer:
                self._executer.shutdown(False)
        except:
            pass

    def send_notifiy(self, _id: str, data: str):
        cur = self.Connection.cursor()
        cur.execute(f'notify "{_id}", %s;', (data,))
        cur.close()

    def listen(self, _id: str):
        cur = self.Connection.cursor()
        cur.execute(f'LISTEN "{_id}";')
        cur.close()

    def poll(self):
        self.Connection.poll()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        self._close()

    def __del__(self):
        self._close()
        self._executer.shutdown(True)

    async def begin_async(self):
        await self.execute_async('begin')

    def begin(self):
        self.execute('begin')

    async def prepared_transaction_async(self):
        from uuid import uuid4
        _id = str(uuid4()).replace('-', '')
        await self.execute_async('prepare transaction %s', (_id,))
        return _id

    def prepared_transaction(self):
        from uuid import uuid4
        _id = str(uuid4()).replace('-', '')
        self.execute('prepare transaction %s', (_id,))
        return _id

    async def commit_prepared_async(self, _id):
        return await self.execute_async('commit prepared %s', (_id,))

    def commit_prepared(self, _id):
        return self.execute('commit prepared %s', (_id,))

    async def rollback_prepared_async(self, _id):
        return await self.execute_async('rollback prepared %s', (_id,))

    def rollback_prepared(self, _id):
        return self.execute('rollback prepared %s', (_id,))
