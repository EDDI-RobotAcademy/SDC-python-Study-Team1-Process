import unittest

from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initCustomProtocol
from mysql.MySQLDatabase import MySQLDatabase
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl


class TestProductService(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testregisterProduct(self):
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



if __name__ == '__main__':
    unittest.main()