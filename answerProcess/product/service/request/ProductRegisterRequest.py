from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductRegisterRequest:
    __productName: str
    __description: str
    __seller: str
    __price: float

    def __init__(self, productName=None, description=None,seller=None,price=None, **kwargs):
        if productName is not None and price is not None:
            self.__productName = productName
            self.__description = description
            self.__seller = seller
            self.__price = price
        elif "__productName" in kwargs and "__price" in kwargs:
            self.__productName = kwargs["__productName"]
            self.__description = kwargs["__description"]
            self.__seller = None
            self.__password = kwargs["__price"]

    def toProduct(self):
        return Product(self.__productName, self.__description, self.__seller, self.__price)
    def setSeller(self, seller):
        self.__seller = seller