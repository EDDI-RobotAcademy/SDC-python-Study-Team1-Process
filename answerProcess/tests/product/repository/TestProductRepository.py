import unittest

from account.entity.Account import Account
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from mysql.MySQLDatabase import MySQLDatabase
from product.ProductServiceImpl import ProductServiceImpl
from product.entity.Product import Product
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl


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

    def testServiceSaveProduct(self):
        service = ProductServiceImpl.getInstance()
        product_data = {
            "productName": "test_product_567890",
            "description": "cabbages",
            "seller": "junghwan",
            "price": "0"
        }
        product = Product(**product_data)

        result = service.registerProduct(product)

        self.assertTrue(result)

    def testFindByProductNumber(self):
        repository = ProductRepositoryImpl.getInstance()

        retrievedProduct = repository.findByProductNumber("2")

        data = ProductServiceImpl.getInstance()
        productData = data.readProductDataByProductNumber(retrievedProduct)
        self.assertIsNotNone(retrievedProduct)

    def testFindAllProducts(self):
        repository = ProductRepositoryImpl.getInstance()
        findProducts = repository.findAllProducts()

        service = ProductServiceImpl.getInstance()
        products = service.getAllProducts()

    def testDeleteProductByNumber(self):
        repository = ProductRepositoryImpl.getInstance()
        repository.deleteByProductNumber("2")

        deletedProduct = repository.findByProductNumber("2")
        self.assertIsNone(deletedProduct)

    def testUpdateProduct(self):
        repository = ProductRepositoryImpl.getInstance()
        updatedProductData = {
            "productName": "newName",
            "description": "newdes",
            "price": "newPrice"
        }
        print(f"updatedProductData: {updatedProductData}")
        updatedProduct = Product(**updatedProductData)
        repository.updateProductInfo(updatedProduct, "3")

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