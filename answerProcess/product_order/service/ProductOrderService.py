import abc


class ProductOrderService(abc.ABC):
    @abc.abstractmethod
    def orderList(self):
        pass

    @abc.abstractmethod
    def orderRegister(self):
        pass

    @abc.abstractmethod
    def orderRemove(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def orderRead(self, *args, **kwargs):
        pass
    