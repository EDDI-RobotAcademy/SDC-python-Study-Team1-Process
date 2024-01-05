from dataclasses import dataclass


@dataclass
class ProgramQuitResponse:
    __isSuccess: bool

    def getIsSuccess(self):
        return self.__isSuccess