from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductRegisterRequest:
    __productName: str
    __discription: str
    __seller: str
    def toProduct(self):
        return Product(self.__productName, self.__discription, self.__seller)
