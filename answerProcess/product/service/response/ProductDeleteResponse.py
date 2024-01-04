from dataclasses import dataclass


@dataclass
class ProductDeleteResponse:
    __isSuccess: bool

    def getIsSuccess(self):
        return self.__isSuccess



