from dataclasses import dataclass


@dataclass
class ProductReadResponse:
    __productId: int
    __productName: str
    __productPrice: float
    __productDetails: str
    __seller: str

    def __init__(self,productId: int, productName: str, productDetails: str, seller: str, productPrice: float):
        self.__productId = productId
        self.__productName = productName
        self.__productDetails = productDetails
        self.__seller = seller
        self.__productPrice = productPrice