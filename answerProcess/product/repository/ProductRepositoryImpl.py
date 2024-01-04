from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

from product.entity.Product import Product
from product.repository.ProductRepository import ProductRepository
# from product.service.response.ProductListResponse import ProductListResponse


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

        if session is not None:
            try:
                session.add(product)
                session.commit()

            print(f"상품 이름: {product.getProductName()}")
            return product

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def findByProductNumber(self, productNumber):

        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        print(dir(productNumber))
        print(f"productNumber: {productNumber}")
        return session.query(Product).filter_by(_Product__productNumber=productNumber).first()

    # def findAllProducts(self):
    #     dbSession = sessionmaker(bind=self.__instance.engine)
    #     session = dbSession()
    #     list = []
    #     for product in session.query(Product).all():
    #         response = ProductListResponse(product.getProductNumber(), product.getProductName(),
    #                                        product.getDescription(), product.getSeller(), product.getPrice())
    #         list.append(response)
    #     return list

    def deleteByProductNumber(self, productNumber):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        product = session.query(Product).filter_by(_Product__productNumber=productNumber).first()
        if product:
            session.delete(product)
            session.commit()

    # def updateProductInfo(self, product):
    #     dbSession = sessionmaker(bind=self.__instance.engine)
    #     session = dbSession()
    #
    #     existingProduct = session.query(Product).filter_by(_Product__productNumber=product.getProductNumber()).first()
    #     if existingProduct:
    #         existingProduct.getProductNumber(product.getProductNumber())
    #         existingProduct.setProductName(product.getProductName())
    #         existingProduct.setDescription(product.getDescription())
    #         existingProduct.setPrice(product.getPrice())
    #         session.commit()

    def findByUserInputKeyword(self, keyword):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Product).filter(Product._Product__productName.ilike(f"%{keyword}%")).all()

    def getBoolWithFindByProductNumber(self, productNumber):
        if self.findByProductNumber(productNumber) is not None:
            return False
        else:
            return True
