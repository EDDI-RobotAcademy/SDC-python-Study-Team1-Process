import abc


class AccountRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, account):
        pass

    @abc.abstractmethod
    def update(self, account):
        pass

    @abc.abstractmethod
    def findById(self, Id):
        pass

    @abc.abstractmethod
    def findByAccountId(self, accountId):
        pass

    @abc.abstractmethod
    def deleteByAccountId(self, accountId):
        pass

    @abc.abstractmethod
    def deleteById(self, Id):
        pass

    @abc.abstractmethod
    def getBoolWithFindByAccountId(self, accountId):
        pass
