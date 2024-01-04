from dataclasses import dataclass


@dataclass
class ProductDeleteRequest:
    __productNumber: int
    def __init__(self, productNumber=None, **kwargs):
        if productNumber is not None:
            self.__productNumber = productNumber
        elif "__productNumber" in kwargs:
            self.__productNumber = kwargs["__productNumber"]


    def getProductNumber(self):
        return self.__productNumber

