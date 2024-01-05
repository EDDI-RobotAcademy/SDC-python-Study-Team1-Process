import unittest


from account.entity.Account import Account
from account.service.AccountServiceImpl import AccountServiceImpl
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl

from main import initCustomProtocol, initOrderDomain, initProductDomain, initAccountDomain

from mysql.MySQLDatabase import MySQLDatabase
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from response_generator.service.ResponseGeneratorServiceImpl import ResponseGeneratorServiceImpl


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self.customProtocolRepository = CustomProtocolRepositoryImpl()
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testregisterAccount(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

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
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        accountData = {'__accountId': 'Id', '__password': 'pw'}

        protocolNumber = 2

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        responseForm = responseGenerator(result)
        print(responseForm)

    def testLogoutAccount(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        accountData = {'__accountSessionId': 17}

        protocolNumber = 3

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        responseForm = responseGenerator(result)
        # result = testInstance.execute(2, tuple(requestForm.__dict__.values()))
        print(responseForm)


    def testdelateaccount(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        accountData = {'__accountSessionId': 13}
        protocolNumber = 4

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(accountData)


        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)



if __name__ == '__main__':
    unittest.main()
