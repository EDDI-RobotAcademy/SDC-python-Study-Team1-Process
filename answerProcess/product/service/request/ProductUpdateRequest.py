from dataclasses import dataclass

from product.entity.Product import Product


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

    # def __init__(self, productNumber=-1, productName=None, description=None, seller=None, price=0, **kwargs):
    #     if productName is not None and description is not None:
    #         self.__productNumber = productNumber
    #         self.__productName = productName
    #         self.__description = description
    #         self.__seller = seller
    #         self.__price = price
    #     elif "__productName" in kwargs and "__description" in kwargs:
    #         self.__productNumber = kwargs["__productNumber"]
    #         self.__productName = kwargs["__productName"]
    #         self.__description = kwargs["__description"]
    #         self.__seller = kwargs["__seller"]
    #         self.__price = kwargs["__price"]

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
