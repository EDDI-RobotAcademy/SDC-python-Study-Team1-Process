from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
# pip3 install passlib


Base = declarative_base()

@dataclass
class ProductOrder(Base):
    __tablename__ = 'product_order'

    __id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __accountId: int = Column(Integer, name="account_id")
    __productId: int = Column(Integer, name="product_id")

    def __init__(self, accountId: int, productId: int):
        self.__accountId = accountId
        self.__productId = productId
        
    def getId(self):
        return self.__id

    def getAccountId(self):
        return self.__accountId

    def getProductId(self):
        return self.__productId


