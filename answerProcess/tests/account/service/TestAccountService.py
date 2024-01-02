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

    def testregisterAccount(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        accountData = {'__accountId': 'Id', '__password': 'pw'}
        protocolNumber = 1

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)




    def testLoginAccount(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        accountData = {'__accountId': 'Id', '__password': 'pw'}
        protocolNumber = 2

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        # result = testInstance.execute(2, tuple(requestForm.__dict__.values()))
        print(result)

    def testLogoutAccount(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        accountData = {'__accountSessionId': 1}
        protocolNumber = 4

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        # result = testInstance.execute(2, tuple(requestForm.__dict__.values()))
        print(result)


    def testdelateaccount(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        accountData = {'__accountSessionId': 1}
        protocolNumber = 3

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)


        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
