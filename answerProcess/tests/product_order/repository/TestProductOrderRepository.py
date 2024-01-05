import unittest
from mysql.MySQLDatabase import MySQLDatabase
from product_order.entity.ProductOrder import ProductOrder
from product_order.repository.ProductOrderRepositoryImpl import ProductOrderRepositoryImpl


class TestProductOrderRepository(unittest.TestCase):
    def setUp(self):
        mysqlDatabase = MySQLDatabase.getInstance()
        mysqlDatabase.connect()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def testSaveProductOrderInfo(self):
        repository = ProductOrderRepositoryImpl.getInstance()
        orderInfo = {
            "accountId": "1",
            "productNumber": "2"
        }
        productOrder = ProductOrder(**orderInfo)

        result = repository.saveProductOrderInfo(productOrder)

        self.assertTrue(result)

    def testFindAllProductIdByAccountId(self):
        repository = ProductOrderRepositoryImpl.getInstance()
        result = repository.findAllProductIdByAccountId(1)
        print(f"result: {result}")

    def testRemoveProductsByAccountId(self):
        repository = ProductOrderRepositoryImpl.getInstance()
        result = repository.removeProductsByAccountId(1, 2)
        print(f"result: {result}")

        self.assertTrue(result)

    def testRemoveAllProductsByAccountId(self):
        repository = ProductOrderRepositoryImpl.getInstance()
        repository.removeAllProductsByAccountId(7)


    if __name__ == '__main__':
        unittest.main()