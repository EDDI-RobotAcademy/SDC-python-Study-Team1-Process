from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductRegisterRequest:
    __productName: str
    __description: str
    __seller: str
    __price: str
    def toProduct(self):
        return Product(self.__productName, self.__description, self.__seller, self.__price)