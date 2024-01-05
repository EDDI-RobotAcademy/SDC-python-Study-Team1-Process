from dataclasses import dataclass


@dataclass
class ProductOrderRemoveResponse:
    __isSuccess: bool

    def getIsSuccess(self):
        return self.__isSuccess