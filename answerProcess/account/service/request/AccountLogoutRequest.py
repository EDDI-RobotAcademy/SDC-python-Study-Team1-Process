from dataclasses import dataclass

from account.entity.AccountSession import AccountSession


@dataclass
class AccountLogoutRequest:
    __accountSessionId: int

    def toSession(self):
        return AccountSession(self.__accountSessionId)

    def __init__(self, accountSessionId = None, **kwargs):
        if accountSessionId is not None:
            self.__accountSessionId = accountSessionId
        elif "__accountSessionId" in kwargs:
            self.__accountSessionId = kwargs["__accountSessionId"]

    @classmethod
    def createFromTuple(cls, inputTuple):
        return cls(*inputTuple)

    def getAccountSessionId(self):
        return self.__accountSessionId
