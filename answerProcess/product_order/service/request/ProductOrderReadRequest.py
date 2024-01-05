from dataclasses import dataclass


@dataclass
class ProductOrderReadRequest:
    __productNumber: int
    __accountSessionId: int

    def __init__(self, productNumber=None,accountSessionId=None, **kwargs):
        if productNumber is not None and accountSessionId is not None:
            self.__productNumber = productNumber
            self.__accountSessionId =accountSessionId
        elif "__productNumber" in kwargs and "__accountSessionId" in kwargs:
            self.__productNumber = kwargs["__productNumber"]
            self.__accountSessionId = kwargs["__accountSessionId"]

    def getProductNumber(self):
        return self.__productNumber

    def getAccountSessionId(self):
        return self.__accountSessionId