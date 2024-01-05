import abc


class ProductOrderRepository(abc.ABC):

    @abc.abstractmethod
    def saveProductOrderInfo(self, order):
        pass

    @abc.abstractmethod
    def findAllProductIdByAccountId(self, accountId):
        pass

    def removeProductsByAccountId(self, accountId, productNumber):
        pass

    def removeAllProductsByAccountId(self, accountId):
        pass
