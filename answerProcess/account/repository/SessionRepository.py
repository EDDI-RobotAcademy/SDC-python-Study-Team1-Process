import abc

from account.entity.AccountSession import AccountSession


class SessionRepository(abc.ABC):
    pass

    @abc.abstractmethod
    def save(self, acountSession: AccountSession):
        pass

    @abc.abstractmethod
    def getIdBySessionId(self):
        pass

    @abc.abstractmethod
    def deleteBySessionId(self, sessionId):
        pass

    @abc.abstractmethod
    def resetSession(self):
        pass