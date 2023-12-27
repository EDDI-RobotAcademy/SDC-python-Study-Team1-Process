import abc


class ProductService(abc.ABC):
    @abc.abstractmethod
    def registerProduct(self, *args, **kwargs):
        pass