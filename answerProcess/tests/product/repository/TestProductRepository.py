import unittest

from account.entity.Account import Account
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from mysql.MySQLDatabase import MySQLDatabase
from product.ProductServiceImpl import ProductServiceImpl
from product.entity.Product import Product
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.request.ProductUpdateRequest import ProductUpdateRequest


class TestProductRepository(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testSaveProduct(self):
        repository = ProductRepositoryImpl.getInstance()
        product_data = {
            "productName": "test_product_12343",
            "description": "cabbages",
            "seller": "junghwan",
            "price": "0"
        }
        product = Product(**product_data)

        result = repository.save(product)

        self.assertTrue(result)


    def testFindByProductNumber(self):
        repository = ProductRepositoryImpl.getInstance()

        retrievedProduct = repository.findProductByProductNumber("2")

        data = ProductServiceImpl.getInstance()
        productData = data.readProductDataByProductNumber(retrievedProduct)
        self.assertIsNotNone(retrievedProduct)

    def testFindAllProducts(self):
        repository = ProductRepositoryImpl.getInstance()
        findProducts = repository.findProductByProductNumber()

        service = ProductServiceImpl.getInstance()
        products = service.productList()

    def testDeleteProductByNumber(self):
        repository = ProductRepositoryImpl.getInstance()
        repository.deleteProductByProductNumber("3")

        # deletedProduct = repository.findProductByProductNumber("2")
        # self.assertIsNone(deletedProduct)

    def testUpdate(self):
        repository = ProductRepositoryImpl.getInstance()
        request = ProductUpdateRequest(8, "111", "111", 111)
        result = repository.updateProductInfo(request)
        # self.assertTrue(result)

    #
    # def testFindById(self):
    #     repository = AccountRepositoryImpl.getInstance()
    #     accountData = {
    #         "accountId": "test_user",
    #         "password": "test_password"
    #     }
    #     account = Account(**accountData)
    #     repository.save(account)
    #
    #     retrievedAccount = repository.findById(account.getId())
    #
    #     self.assertIsNotNone(retrievedAccount)
    #     self.assertEqual(retrievedAccount.getAccountId(), accountData["accountId"])
    #
    # def testSameNameSaveAccount(self):
    #     repository = AccountRepositoryImpl.getInstance()
    #     account_data = {
    #         "accountId": "test_user",
    #         "password": "test_password"
    #     }
    #     account = Account(**account_data)
    #
    #     result = repository.save(account)
    #
    #     self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
