from dataclasses import dataclass

from account.entity.Account import Account


@dataclass
class AccountLoginRequest:
    __accountId: str
    __password: str

    def toAccount(self):
        return Account(self.__accountId, self.__password)

