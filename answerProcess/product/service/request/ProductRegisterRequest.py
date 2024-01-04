from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductRegisterRequest:
    __productTitle: str
    __productDetails: str
    __seller: str
    __productPrice: float

    def __init__(self, productTitle=None, productDetails=None, seller=None, productPrice=None, **kwargs):
        if productTitle is not None and productPrice is not None:
            self.__productTitle = productTitle
            self.__productDetails = productDetails
            self.__seller = seller
            self.__productPrice = productPrice
        elif "__productTitle" in kwargs and "__productPrice" in kwargs:
            self.__productTitle = kwargs["__productTitle"]
            self.__productDetails = kwargs["__productDetails"]
            self.__seller = None
            self.__productPrice = kwargs["__productPrice"]

    def toProduct(self):
        return Product(self.__productTitle, self.__productDetails, self.__seller, self.__productPrice)
    def setSeller(self, seller):
        self.__seller = seller