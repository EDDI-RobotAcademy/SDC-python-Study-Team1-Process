import abc


class SessionRepository(abc.ABC):
    pass

    @abc.abstractmethod
    def getIdBySessionId(self):
        pass
