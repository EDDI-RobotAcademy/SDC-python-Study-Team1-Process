import unittest

from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initCustomProtocol, initEachDomain, initAccountDomain, initProductDomain, initOrderDomain
from mysql.MySQLDatabase import MySQLDatabase
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from response_generator.service.ResponseGeneratorServiceImpl import ResponseGeneratorServiceImpl


class TestProductOrderService(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testProductOrderRegister(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        productPurchaseRequestData = {
            '__accountSessionId': 13,
            '__productNumber': 3
        }
        protocolNumber = 9

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(productPurchaseRequestData)
        print(f"type(requestForm) = {type(requestForm)}")
        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)
        print(f"type(result): {type(result)}")
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        print(result)
        responseForm = responseGenerator(result)
        print(f"responseForm: {responseForm}")

    def testProductOrderList(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        productPurchaseRequestData = {
            '__accountSessionId': 22
        }
        protocolNumber = 11

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(productPurchaseRequestData)
        print(f"type(requestForm) = {type(requestForm)}")
        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)
        print(f"type(result): {type(result)}")
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        print(result)
        responseForm = responseGenerator(result)
        print(f"responseForm: {responseForm}")

    def testOrderDelete(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        orderData = {'__accountSessionId': -1,
            '__productNumber': 23}
        protocolNumber = 13

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(orderData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        print(result)
        responseForm = responseGenerator(result)
        print(f"responseForm: {responseForm}")

    def testProductOrderRead(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()

        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        orderData = {'__accountSessionId': 5,
                    '__productOrderNumber': 9}
        protocolNumber = 12

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(orderData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        print(result)
        responseForm = responseGenerator(result)
        print(f"responseForm: {responseForm}")

    if __name__ == '__main__':
        unittest.main()