import unittest
from account.entity.Account import Account
from account.service.AccountServiceImpl import AccountServiceImpl
from mysql.MySQLDatabase import MySQLDatabase



class TestAccountRepository(unittest.TestCase):

def testdelateaccount(self):
    service = AccountServiceImpl.getInstance()
    account_data = {
        "accountId": "test_user",
        "password": "test_password"
    }
    account = Account(**account_data)

    result = service.deleteAccount(account)

    self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()