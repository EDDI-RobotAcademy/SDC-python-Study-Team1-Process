from dataclasses import dataclass



@dataclass
class ProductUpdateRequest:
    __productNumber: int
    __productTitle: str
    __productDetails: str
    __productPrice: int


    def __init__(self, productNumber=None, productTitle=None, productDetails=None, productPrice=None, **kwargs):
        if productTitle is not None and productPrice is not None:
            self.__productNumber = productNumber
            self.__productTitle = productTitle
            self.__productDetails = productDetails
            self.__productPrice = productPrice
        elif "__productTitle" in kwargs and "__productPrice" in kwargs:
            self.__productNumber = kwargs["__productNumber"]
            self.__productTitle = kwargs["__productTitle"]
            self.__productDetails = kwargs["__productDetails"]
            self.__productPrice = kwargs["__productPrice"]
    @classmethod
    def createFromTuple(cls, inputTuple):
        return cls(*inputTuple)

    def getProductNumber(self):
        return self.__productNumber

    def getProductTitle(self):
        return self.__productTitle

    def getProductDetails(self):
        return self.__productDetails

    def getProductPrice(self):
        return self.__productPrice