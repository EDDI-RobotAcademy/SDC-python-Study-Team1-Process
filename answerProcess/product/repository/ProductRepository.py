import abc


class ProductRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, product):
        pass

    def findByProductNumber(self, productNumber):
        pass

    def findAllProducts(self):
        pass

    def deleteByProductNumber(self, productNumber):
        pass

    def updateProductInfo(self, product, productNumber):
        pass