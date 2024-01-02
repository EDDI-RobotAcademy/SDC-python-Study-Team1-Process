from sqlalchemy.orm import sessionmaker

from product_order.entity.ProductOrder import ProductOrder
from product_order.repository.ProductOrderRepository import ProductOrderRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError


class OrderRepositoryImpl(ProductOrderRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    def __init__(self):
        print("TaskManageRepository 생성자 호출")
        self.__receiverTask = None
        self.__transmitterTask = None

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

    def findAccountId(self, accountId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(ProductOrder).filter_by(_ProductOrder__accountId=accountId).first()

    def findAllProductIdByAccountId(self, accountId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        accountIdList = session.query(ProductOrder).filter_by(_ProductOrder__accountId=accountId).all()
        productIdList = []
        for id in accountIdList:
            productIdList.append(id.getProductId())

        return productIdList