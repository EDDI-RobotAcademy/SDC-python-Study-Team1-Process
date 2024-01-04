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

    def saveProductOrderInfo(self, orderInfo):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            session.add(orderInfo)
            session.commit()

            print(f"order - id: {orderInfo.getId()}")
            return orderInfo

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
            productIdList.append(id.productNumber())

        return productIdList

    def removeProductsByAccountId(self, sessionId, productId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        products = session.query(ProductOrder).filter_by(_ProductOrder__accountId=sessionId,
                                                         _ProductOrder__productId=productId).all()

        if products:
            for product in products:
                session.delete(product)
                session.commit()
            response = True
            print("주문 취소 완료")
        else:
            response = False
            print("주문을 취소할 수 없습니다.")

        return response
