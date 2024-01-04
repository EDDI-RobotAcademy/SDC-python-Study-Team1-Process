from dataclasses import dataclass


@dataclass
class ProductRegisterResponse:
    __isSuccess: bool

    def getIsSuccess(self):
        return self.__isSuccess