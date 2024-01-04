import abc


class ProductRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, product):
        pass

    def findProductByProductNumber(self, productNumber):
        pass

    def findAllProducts(self):
        pass

    def deleteProductByProductNumber(self, productNumber):
        pass

    def findByUserInputKeyword(self, keyword):
        pass