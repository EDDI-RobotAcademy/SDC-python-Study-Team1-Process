from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from passlib.hash import pbkdf2_sha256

Base = declarative_base()

@dataclass
class Session(Base):
    __tablename__: str = "session"

    __id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __sessionId: int = Column(Integer, name="session_id")

    def __init__(self, sessionId: int):
        self.__sessionId = sessionId
