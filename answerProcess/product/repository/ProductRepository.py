import abc


class ProductRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, product):
        pass
    @abc.abstractmethod
    def findProductByProductNumber(self, productNumber):
        pass
    @abc.abstractmethod
    def findAllProducts(self):
        pass
    @abc.abstractmethod
    def deleteProductByProductNumber(self, productNumber):
        pass
    def deleteAllProductBySeller(self, seller):
        pass
    @abc.abstractmethod
    def updateProductInfo(self, product):
        pass
