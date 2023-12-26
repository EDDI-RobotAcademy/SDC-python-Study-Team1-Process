import unittest
from account.entity.Account import Account
from account.service.AccountServiceImpl import AccountServiceImpl
from mysql.MySQLDatabase import MySQLDatabase



class TestAccountService(unittest.TestCase):

    def testdelateaccount(self):

        service = AccountServiceImpl.getInstance()

        account_data = {
            "accountId": "test_user",
        }
        account = Account(**account_data)

        result = service.deleteAccount("test_user")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

