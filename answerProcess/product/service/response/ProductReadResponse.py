from dataclasses import dataclass


@dataclass
class ProductReadResponse:
    __productNumber: int
    __productTitle: str
    __productPrice: int
    __productDetails: str
    __seller: str

    def __init__(self, productNumber: int, productTitle: str, productPrice: int ,productDetails: str, seller: str):
        self.__productNumber = productNumber
        self.__productTitle = productTitle
        self.__productPrice = productPrice
        self.__productDetails = productDetails
        self.__seller = seller


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
