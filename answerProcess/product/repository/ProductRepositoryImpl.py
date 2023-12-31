from sqlalchemy.orm import sessionmaker

from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

from product.entity.Product import Product
from product.repository.ProductRepository import ProductRepository

class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    def __init__(self):
        print("ProductRepositoryImpl 생성자 호출")


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

                print(f"상품 이름: {product.getProductTitle()}")
                return product

            except SQLAlchemyError as exception:
                session.rollback()
                print(f"DB 저장 중 에러 발생: {exception}")
                return None
        else:
            return None

    def findProductByProductNumber(self, productNumber):

        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Product).filter_by(_Product__productNumber=productNumber).first()

    def findAllProducts(self):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Product).all()

    def deleteProductByProductNumber(self, productNumber):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        product = session.query(Product).filter_by(_Product__productNumber=productNumber).first()
        if product is not None:
            session.delete(product)
            session.commit()
            return True
        else:
            return False

    def deleteAllProductBySeller(self, seller):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        foundProduct = session.query(Product).filter_by(_Product__seller=seller).all()

        if foundProduct:
            for product in foundProduct:
                session.delete(product)
                session.commit()

    def updateProductInfo(self, product):
        print(f"product: {product}")
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        existingProduct = session.query(Product).filter_by(_Product__productNumber=product.getProductNumber()).first()
        print(f"existingProduct: {existingProduct}")

        if existingProduct is not None:
            existingProduct.editProduct(product.getProductTitle(),product.getProductPrice(), product.getProductDetails())
            session.commit()
            return True
        else:
            return False