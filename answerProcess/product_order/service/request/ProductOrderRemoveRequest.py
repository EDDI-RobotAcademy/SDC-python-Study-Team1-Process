from dataclasses import dataclass


@dataclass
class ProductOrderRemoveRequest:
    __productNumber: int
    __accountSessionId: int

    def __init__(self, productNumber=-1, accountSessionId=-1, **kwargs):
        if "__productNumber" in kwargs and "__accountSessionId" in kwargs:
            self.__productNumber = kwargs["__productNumber"]
            self.__accountSessionId = kwargs["__accountSessionId"]
        else:
            self.__productNumber = productNumber
            self.__accountSessionId = accountSessionId

    @classmethod
    def createFromTuple(cls, inputTuple):
        return cls(*inputTuple)

    def getAccountId(self):
        return self.__accountSessionId

    def getProductNumber(self):
        return self.__productNumber

