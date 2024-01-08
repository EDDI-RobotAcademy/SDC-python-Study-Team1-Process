import abc


class ProductOrderRepository(abc.ABC):

    @abc.abstractmethod
    def saveProductOrderInfo(self, order):
        pass

    @abc.abstractmethod
    def findAllProductIdByAccountId(self, accountId):
        pass

    def removeProductsOrderByAccountId(self, accountId, productNumber):
        pass

    def removeAllProductsOrdersByAccountId(self, accountId):
        pass

    def removeAllProductsOrderByProductNumber(self, productNumber):
        pass
