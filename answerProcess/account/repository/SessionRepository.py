import abc


class SessionRepository(abc.ABC):
    pass

    @abc.abstractmethod
    def getAccountBySessionId(self):
        pass
