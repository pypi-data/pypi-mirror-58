from ._querydata import _QeryData


class QueryData(list):

    def __init__(self, datas, rowcount):
        super().__init__([_QeryData(x) for x in datas])
        self.rowcount = rowcount
