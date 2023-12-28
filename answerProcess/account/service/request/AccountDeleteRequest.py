from dataclasses import dataclass

from account.entity.Account import Account


@dataclass
class AccountDeleteRequest:
    __id: int


    def __inint__(self, id: int):
        self.__id = id

    def getAccountId(self):
        return self.__id

