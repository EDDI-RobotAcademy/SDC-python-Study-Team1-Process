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

        result = testInstance.execute(1, sample)

        self.assertIsNone(result)


    def testLoginAccountSession(self):
        service = AccountServiceImpl.getInstance()
        # initCustomProtocol()
        # testInstance = CustomProtocolRepositoryImpl.getInstance()
        # accountData = {
        #     "accountId": "test_user111",
        #     "password": "test_password"
        # }

        accountUnuqe = ("testUser", "testPassword")
        result = service.loginAccount(accountUnuqe)
        self.assertIsNone(result)

    def testdelateaccount(self):

        service = AccountServiceImpl.getInstance()

        # account_data = {
        #     "accountId": "test_user",
        # }
        # account = Account(**account_data)
        accountUnuqe = ('9')
        result = service.deleteAccount(accountUnuqe)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
