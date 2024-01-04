import abc


class ProductService(abc.ABC):
    @abc.abstractmethod
    def productRegister(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def productRead(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def productList(self):
        pass
    @abc.abstractmethod
    def productDelete(self, *args, **kwargs):
        pass
    @abc.abstractmethod
    def productUpdate(self, *args, **kwargs):
        pass
