from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

from product.entity.Product import Product
from product.repository.ProductRepository import ProductRepository
from product.service.response.ProductListResponse import ProductListResponse


class ProductRepositoryImpl(ProductRepository):
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

    def save(self, product):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        if self.getBoolWithFindByProductName(product.getProductName()):
            try:
                session.add(product)
                session.commit()

                print(f"상품 이름: {product.getProductName()}")
                return product

            except SQLAlchemyError as exception:
                session.rollback()
                print(f"DB 저장 중 에러 발생: {exception}")
                return None
        else:
            print("중복")

    # def update(self, account):
    #     dbSession = sessionmaker(bind=self.__instance.engine)
    #     session = dbSession()
    #
    #     # protected 키워드는 이런데서 사용합니다.
    #     existingAccount = session.query(Account).filter_by(_Account__accountId=account.getAccountId()).first()
    #     if existingAccount:
    #         existingAccount.setPassword(account.getPassword())
    #         session.commit()
    #
    # def findById(self, id):
    #     dbSession = sessionmaker(bind=self.__instance.engine)
    #     session = dbSession()
    #
    #     return session.query(Account).filter_by(_Account__id=id).first()
    #
    def findByProductNumber(self, productNumber):

        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        print(dir(productNumber))

        return session.query(Product).filter_by(_Product__productNumber=productNumber).first()

    def findAllProducts(self):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        list = []
        for product in session.query(Product).all():
            response = ProductListResponse(product.getProductNumber(), product.getProductName(),
                                           product.getDescription(), product.getSeller(), product.getPrice())
            list.append(response)

            # print(f"1. 상품 번호: {product.getProductNumber()}")
            # print(f"2. 상품 이름: {product.getProductName()}")
            # print(f"3. 상품 설명: {product.getDescription()}")
            # print(f"4. 판매자: {product.getSeller()}")
            # print(f"5. 상품 가격: {product.getPrice()}\n")

        return list

    def deleteByProductNumber(self, productNumber):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        product = session.query(Product).filter_by(_Product__productNumber=productNumber).first()
        if product:
            session.delete(product)
            session.commit()

    def getBoolWithFindByProductName(self, productName):
        if self.findByProductName(productName) is not None:
            return False
        else:
            return True