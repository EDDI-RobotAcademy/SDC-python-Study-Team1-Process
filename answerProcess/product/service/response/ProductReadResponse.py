from dataclasses import dataclass


@dataclass
class ProductReadResponse:
    __productNumber: int
    __productTitle: str
    __productPrice: float
    __productDetails: str
    __seller: str

    def __init__(self,productNumber: int, productTitle: str, productDetails: str, seller: str, productPrice: float):
        self.__productNumber = productNumber
        self.__productTitle = productTitle
        self.__productDetails = productDetails
        self.__seller = seller
        self.__productPrice = productPrice

    def getProductNumber(self):
        return self.__productNumber

    def getProductTitle(self):
        return self.__productTitle

    def getProductPrice(self):
        return self.__productPrice

    def getProductDetails(self):
        return self.__productDetails

    def getSeller(self):
        return self.__seller

    def __iter__(self):
        yield "__productNumber", self.__productNumber
        yield "__productTitle", self.__productTitle
        yield "__productPrice", self.__productPrice
        yield "__productDetails", self.__productDetails
        yield "__seller", self.__seller
