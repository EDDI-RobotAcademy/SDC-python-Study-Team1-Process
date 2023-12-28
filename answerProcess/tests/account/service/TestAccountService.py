import unittest


from account.entity.Account import Account
from account.service.AccountServiceImpl import AccountServiceImpl
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initCustomProtocol
from mysql.MySQLDatabase import MySQLDatabase
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl


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
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        accountData = {'__accountId': 'id', '__password': 'pw'}
        protocolNumber = 2

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)

        sample = ("testUser", "testPassword")

        result = testInstance.execute(2, tuple(requestForm.__dict__.values()))
        print(result)

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
