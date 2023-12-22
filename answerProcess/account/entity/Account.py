from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from passlib.hash import pbkdf2_sha256
# pip3 install passlib

# db engine 에서 추적하기 위해 넣어 줌
Base = declarative_base()


@dataclass
# python 에서 () 안은 상속
class Account(Base):
    __tablename__ = 'account'

# column = desc account;
# __는 private = 변경하지 못 하도록
# __로 사용하려면 name 까지만 쓰면 됨
    __id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __accountId: str = Column(String, name="account_id")
    __password: str = Column(String, name="password")

    def __init__(self, accountId: str, password: str):
        self.__accountId = accountId
        self.__password = pbkdf2_sha256.hash(password)

    def checkPassword(self, password):
        return pbkdf2_sha256.verify(password, self.__password)

    def getId(self):
        return self.__id

    def getAccountId(self):
        return self.__accountId

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

