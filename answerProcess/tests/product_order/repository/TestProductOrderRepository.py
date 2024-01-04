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
            "productId": "1"
        }
        productOrder = ProductOrder(**orderInfo)

        result = repository.saveProductOrderInfo(productOrder)

        self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()