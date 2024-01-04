from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductListResponse:
    __productNumber: int
    __productTitle: str
    __productPrice: int

    def __init__(self,productNumber: int, productTitle: str, productPrice: int):
        self.__productNumber = productNumber
        self.__productTitle = productTitle
        self.__productPrice = productPrice

    def __iter__(self):
        yield "__productNumber", self.__productNumber
        yield "__productTitle", self.__productTitle
        yield "__productPrice", self.__productPrice
