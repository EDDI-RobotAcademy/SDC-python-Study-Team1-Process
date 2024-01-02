import abc


class ProductOrderRepository(abc.ABC):

    @abc.abstractmethod
    def saveProductOrderInfo(self, orderInfo):
        pass

    @abc.abstractmethod
    def findAccountId(self, accountId):
        pass