from dataclasses import dataclass

from account.entity.Account import Account


@dataclass
class AccountDeleteRequest:
    __accountId: str

    def toDeleteAccount(self):
        return Account(self.__accountId)

