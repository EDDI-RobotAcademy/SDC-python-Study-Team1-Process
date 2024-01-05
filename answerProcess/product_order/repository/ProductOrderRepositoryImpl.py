from sqlalchemy.orm import sessionmaker

from product_order.entity.ProductOrder import ProductOrder
from product_order.repository.ProductOrderRepository import ProductOrderRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError


class ProductOrderRepositoryImpl(ProductOrderRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    def __init__(self):
        print("ProductOrderRepository 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def saveProductOrderInfo(self, order):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            session.add(order)
            session.commit()

            print(f"order - id: {order.getId()}")
            return order

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def findAllProductIdByAccountId(self, accountId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        accountIdList = session.query(ProductOrder).filter_by(_ProductOrder__accountId=accountId).all()
        productIdList = []
        for id in accountIdList:
            productIdList.append(id.getProductNumber())

        return productIdList

    def removeProductsByAccountId(self, accountId, productNumber):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()



        foundProductOrder = session.query(ProductOrder).filter_by(_ProductOrder__accountId=accountId,
                                                                  _ProductOrder__productNumber=productNumber).all()

        if foundProductOrder:
            for product in foundProductOrder:
                session.delete(product)
                session.commit()
            response = True
        else:
            response = False

        return response

