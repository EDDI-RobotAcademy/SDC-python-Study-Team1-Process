from dataclasses import dataclass

from account.entity.Account import Account


@dataclass
class AccountLoginRequest:
    __accountId: str
    __password: str

    def getPassword(self):
        return self.__password

