from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from passlib.hash import pbkdf2_sha256

from account.entity.Account import Account
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl

# pip3 install passlib

# db engine 에서 추적하기 위해 넣어 줌
Base = declarative_base()


@dataclass
# python 에서 () 안은 상속
class Product(Base):
    __tablename__ = 'product'

    # column = desc account;
    # __는 private = 변경하지 못 하도록
    # __로 사용하려면 name 까지만 쓰면 됨
    __productNumber: int = Column(Integer, primary_key=True, autoincrement=True, name="product_number")
    __productTitle: str = Column(String, name="product_name")
    __productDetails: str = Column(String, name="description")
    __seller: str = Column(String, name="seller")
    __productPrice: int = Column(String, name="price")

    def __init__(self, productTitle: str, productDetails: str, seller: str, productPrice: int):
        self.__productTitle = productTitle
        self.__productDetails = productDetails
        self.__seller = seller
        self.__productPrice = productPrice

    def getProductNumber(self):
        return self.__productNumber

    def getProductTitle(self):
        return self.__productTitle

    def getProductDetails(self):
        return self.__productDetails

    def getSeller(self):
        return self.__seller

    def getProductPrice(self):
        return self.__productPrice

    def setProductNumber(self, productNumber):
        self.__productNumber = productNumber

    def setProductTitle(self, productTitle):
        self.__productTitle = productTitle

    def setProductDetails(self, productDetails):
        self.__productDetails = productDetails

    def setSeller(self, seller):
        self.__seller = seller

    def setProductPrice(self, productPrice):
        self.__productPrice = productPrice

    def editProduct(self, _newProductTitle: str, _newProductPrice: int, _newProductDetails: str):
        self.__productTitle = _newProductTitle
        self.__productPrice = _newProductPrice
        self.__productDetails = _newProductDetails
