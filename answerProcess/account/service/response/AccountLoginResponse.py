from dataclasses import dataclass


@dataclass
class AccountLoginResponse:
    __id: int

    def getId(self):
        return self.__id
