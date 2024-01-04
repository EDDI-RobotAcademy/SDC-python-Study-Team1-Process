import abc


class ProductOrderRepository(abc.ABC):

    @abc.abstractmethod
    def saveProductOrderInfo(self, orderInfo):
        pass

    @abc.abstractmethod
    def findAllProductIdByAccountId(self, accountId):
        pass