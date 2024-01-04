from dataclasses import dataclass


@dataclass
class ProductOrderRegisterResponse:
    __isSuccess: bool

    def getIsSuccess(self):
        return self.__isSuccess

