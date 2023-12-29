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
    __productName: str = Column(String, name="product_name")
    __description: str = Column(String, name="description")
    __seller: str = Column(String, name="seller")
    __price: float = Column(String, name="price")

    def __init__(self, productNumber: int, productName: str, description: str, seller: str, price: float):
        self.__productNumber = productNumber
        self.__productName = productName
        self.__description = description
        self.__seller = seller
        self.__price = price

    def getProductNumber(self):
        return self.__productNumber
    def getProductName(self):
        return self.__productName

    def getDescription(self):
        return self.__description

    def getSeller(self):
        return self.__seller

    def getPrice(self):
        return self.__price

    def setProductName(self, productNumber):
        self.__productNumber = productNumber
    def setProductName(self, productName):
        self.__productName = productName

    def setDescription(self, description):
        self.__description = description

    def setSeller(self, seller):
        self.__seller = seller

    def setPrice(self, price):
        self.__price = price