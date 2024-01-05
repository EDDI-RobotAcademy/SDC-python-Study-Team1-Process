import unittest

from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from main import initCustomProtocol, initAccountDomain, initProductDomain, initOrderDomain
from mysql.MySQLDatabase import MySQLDatabase
from product.service.ProductServiceImpl import ProductServiceImpl
from product.entity.Product import Product
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.request.ProductDeleteRequest import ProductDeleteRequest
from product.service.request.ProductUpdateRequest import ProductUpdateRequest
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
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
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()

        testInstance = CustomProtocolRepositoryImpl.getInstance()

        protocolNumber = 5

        result = testInstance.execute(protocolNumber)
        print(result)
        print(f"type(result): {type(result)}")
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        print(result)
        responseForm = responseGenerator(result)
        print(f"responseForm: {responseForm}")

    def testRegisterProduct(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()

        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        productData = {
            '__productTitle': '망할1',
            '__productDetails': '어렵다',
            '__productPrice': 10000}
        protocolNumber = 6

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(productData)

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)
        print(f"type(result): {type(result)}")
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

        responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
        print(result)
        responseForm = responseGenerator(result)
        print(f"responseForm: {responseForm}")

    def testReadProduct(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

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
    def testDeleteProduct(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()

        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        productdata = {
            '__productNumber': 13
        }
        protocolNumber = 10

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

    def testUpdateProduct(self):
        initAccountDomain()
        initProductDomain()
        initOrderDomain()

        initCustomProtocol()

        testInstance = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()
        updateData = {
            "__productNumber": 13,
            "__productTitle": "111",
            "__productDetails": "111",
            "__productPrice": 111
        }
        protocolNumber = 8

        requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
        requestForm = requestGenerator(updateData)
        print(f"requestForm: {requestForm}")

        result = testInstance.execute(protocolNumber, tuple(requestForm.__dict__.values()))
        print(result)
        print(f"type(result): {type(result)}")


if __name__ == '__main__':
    unittest.main()
