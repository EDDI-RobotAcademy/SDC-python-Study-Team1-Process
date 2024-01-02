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

    def testUpdate(self):
        service = ProductServiceImpl.getInstance()
        repository = ProductRepositoryImpl.getInstance()
        foundProduct = repository.findByProductNumber("3")
        print(f"foundProduct: {foundProduct}")

        if foundProduct is not None:
            productUpdateRequest ={"__productNumber": foundProduct.getProductNumber(),
                                   "__productName": "test_update",
                                   "__description": "test",
                                   "__seller": "test_seller",
                                   "__price": 100.0
                                   }

            print(f"type{productUpdateRequest}")
            result = service.updateProduct(productUpdateRequest)

            self.assertTrue(result)

    # def testUpdate(self):
    #     service = ProductServiceImpl.getInstance()
    #     repository = ProductRepositoryImpl.getInstance()
    #     foundProduct = repository.findByProductNumber("3")
    #     print(f"foundProduct: {foundProduct}")
    #
    #     if foundProduct is not None:
    #         productUpdateData = {
    #             foundProduct.getProductNumber(),
    #             foundProduct.getProductName("test_update"),
    #             foundProduct.getDescription("test"),
    #             foundProduct.getSeller("test_seller"),
    #             foundProduct.getPrice("100.0")
    #         }
    #         productUpdateRequest = ProductUpdateRequest(**productUpdateData)
    #
    #         result = service.updateProduct(productUpdateRequest)
    #
    #         self.assertTrue(result)


# def testUpdateProduct(self):
    #     repository = ProductRepositoryImpl.getInstance()
    #     updatedProductData = {
    #         "productName": "newName",
    #         "description": "newdes",
    #         "price": "newPrice"
    #     }
    #     print(f"updatedProductData: {updatedProductData}")
    #     updatedProduct = Product(**updatedProductData)
    #     repository.updateProductInfo(updatedProduct, "3")

    # def testServiceUpdateProduct(self):
    #     service = ProductServiceImpl.getInstance()
    #     repository = ProductRepositoryImpl.getInstance()
    #     updatedProductData = {
    #         "productNumber": repository.findByProductNumber('3'),
    #         "productName": "newName1",
    #         "description": "newdes1",
    #         "price": "newPrice1"
    #     }
    #     print(f"updatedProductData: {updatedProductData}")
    #     updatedProduct = Product(**updatedProductData)
    #     service.productUpdate(updatedProduct)

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