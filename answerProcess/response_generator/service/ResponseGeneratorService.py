import abc
class ResponseGeneratorService(abc.ABC):
    @abc.abstractmethod
    def findResponseGenerator(self, protocolNumber):
        pass
    @abc.abstractmethod
    def generateAccountRegisterResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountLoginResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountDeleteResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountLogoutResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductListResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductRegisterResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductReadResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductUpdateResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductOrderRegisterResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductRemoveResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductOrderListResponse(self, arguments):
        pass