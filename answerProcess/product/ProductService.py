import abc


class ProductService(abc.ABC):
    @abc.abstractmethod
    def registerProduct(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def readProductDataByProductNumber(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def updateProduct(self, *args, **kwargs):
        pass
