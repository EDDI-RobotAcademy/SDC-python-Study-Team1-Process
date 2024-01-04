import unittest

from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initCustomProtocol
from mysql.MySQLDatabase import MySQLDatabase
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from response_generator.service.ResponseGeneratorServiceImpl import ResponseGeneratorServiceImpl
from product.service.response.ProductReadResponse import ProductReadResponse


class TestProductService(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testListProduct(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()

        protocolNumber = 5

        result = testInstance.execute(protocolNumber)
        print(result)

    def testRegisterProduct(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        productdata = {
            '__productTitle': 'test_product_title',
            '__productContent': 'test_product_content',
            '__productPrice': 10000}
        protocolNumber = 6

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(productdata)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)


    def testReadProduct(self):
        initCustomProtocol()
        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        productdata = {
            '__productNumber': 4
        }
        protocolNumber = 7

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(productdata)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)
        print(f"type(result): {type(result)}")
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        print(result)
        responseForm = responseGenerator(result)
        print(f"responseForm: {responseForm}")






if __name__ == '__main__':
    unittest.main()