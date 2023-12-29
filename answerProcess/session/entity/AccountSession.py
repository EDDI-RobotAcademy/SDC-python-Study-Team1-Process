from dataclasses import dataclass
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declarative_base
from passlib.hash import pbkdf2_sha256

Base = declarative_base()

@dataclass
class AccountSession(Base):
    __tablename__: str = "session"

    __id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __sessionId: int = Column(Integer, name="session_id")
    #__expiration_time: datetime = Column(DateTime, name="expiration_time")

    def __init__(self, sessionId):
        self.__sessionId = sessionId

    def getSessionId(self) :
        return self.__sessionId

