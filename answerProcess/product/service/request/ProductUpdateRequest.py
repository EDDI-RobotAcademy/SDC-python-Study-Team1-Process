from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductUpdateRequest:
    __new_productName: str
    __new_description: str
    __new_price: int

    def __init__(self, productName: str, description: str, price: int):
        self.__id = id
        self.__new_productName = productName
        self.__new_description = description
        self.__new_price = price

    def getNewProductName(self):
        return self.__new_productName

    def getNewDescription(self):
        return self.__new_description

    def getNewPrice(self):
        return self.__new_price

    def toProduct(self):
        return Product(self.__new_productName, self.__new_description, self.__new_price)