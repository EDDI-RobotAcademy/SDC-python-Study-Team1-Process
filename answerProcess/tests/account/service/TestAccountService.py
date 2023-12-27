import unittest

from account.entity.Account import Account
from account.service.AccountServiceImpl import AccountServiceImpl
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initCustomProtocol
from mysql.MySQLDatabase import MySQLDatabase


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self.customProtocolRepository = CustomProtocolRepositoryImpl()
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testLoginAccount(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        accountData = {
            "accountId": "test_user111",
            "password": "test_password"
        }

        sample = ("testUser", "testPassword")

        result = testInstance.execute(2, **accountData)

        print(result)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()