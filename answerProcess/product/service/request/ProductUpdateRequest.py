from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductUpdateRequest:
    __productNumber: int
    __productName: str
    __description: str
    __seller: str
    __price: float


    def __init__(self, productName: str, description: str, seller: str, price: int):
        self.__productName = productName
        self.__description = description
        self.__seller = seller
        self.__price = price

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

    def toProduct(self):
        return Product(self.__productName, self.__description, self.__seller, self.__price)

    @classmethod
    def createFromTuple(cls, inputTuple):
        return cls(*inputTuple)

    def getProductNumber(self):
        return self.__productNumber

    def getProductName(self):
        return self.__productName

    def getSeller(self):
        return self.__seller

    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price
