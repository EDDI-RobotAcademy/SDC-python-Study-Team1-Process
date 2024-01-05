from dataclasses import dataclass


@dataclass
class ProductUpdateResponse:
    __isSuccess: bool

    def getIsSuccess(self):
        return self.__isSuccess