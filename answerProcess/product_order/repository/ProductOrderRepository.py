import abc


class ProductOrderRepository(abc.ABC):

    @abc.abstractmethod
    def saveProductOrderInfo(self, order):
        pass

    @abc.abstractmethod
    def findAllProductIdByAccountId(self, accountId):
        pass