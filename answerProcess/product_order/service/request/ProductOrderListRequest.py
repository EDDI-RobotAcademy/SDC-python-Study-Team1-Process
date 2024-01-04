class ProductOrderListRequest:
    __accountSessionId: int

    def __init__(self, accountSessionId=None, **kwargs):
        if "__accountSessionId" in kwargs:
            self.__accountSessionId = kwargs["__accountSessionId"]
        else:
            self.__accountSessionId = accountSessionId

    @classmethod
    def createFromTuple(cls, inputTuple):
        return cls(*inputTuple)

    def getSessionId(self):
        return self.__accountSessionId