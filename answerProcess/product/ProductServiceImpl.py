from account.entity.Account import Account
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from product.ProductService import ProductService
from product.entity.Product import Product
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.request.ProductDeleteRequest import ProductDeleteRequest
# from product.service.request.ProductEditRequest import ProductEditRequest
from product.service.request.ProductReadRequest import ProductReadRequest
from product.service.request.ProductRegisterRequest import ProductRegisterRequest
from product.service.response import ProductListResponse
from product.service.response.ProductDeleteResponse import ProductDeleteResponse
# from product.service.response.ProductEditResponse import ProductEditResponse
from product.service.response.ProductReadResponse import ProductReadResponse
from product.service.response.ProductRegisterResponse import ProductRegisterResponse


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repository = repository
        return cls.__instance

    def __init__(self, repository):
        print("ProductServiceImpl 생성자 호출")
        self.__productRepository = ProductRepositoryImpl()
        self.__accountRepository = AccountRepositoryImpl()
        self.__sessionRepository = SessionRepositoryImpl()

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def registerProduct(self, *args, **kwargs):
        cleanedElements = args[0]

        seller = self.__accountRepository.findById(self.__sessionRepository.getIdBySessionId()).getAccountId()
        productRegisterRequest = ProductRegisterRequest(*cleanedElements)
        productRegisterRequest.setSeller(seller)
        data = self.__productRepository.save(productRegisterRequest.toProduct())

        return ProductRegisterResponse(data.getProductName(), data.getDescription(), data.getSeller(), data.getPrice())

    def readProductDataByProductNumber(self, *args, **kwargs):
        cleanedElements = args[0]

        productReadRequest = ProductReadRequest(cleanedElements.getProductNumber())
        data = self.__productRepository.findByProductNumber(productReadRequest.getProductNumber())

        if data:
            productReadResponse = ProductReadResponse(
                data.getProductName(),
                data.getDescription(),
                data.getSeller(),
                data.getPrice())
            return productReadResponse
        else:
            print("상품을 찾을 수 없습니다.")
            return None

    def getAllProducts(self, *args, **kwargs):
         product_list = self.__productRepository.findAllProducts()
         return product_list

    def deleteProduct(self, *args, **kwargs):
        cleanedElements = args[0]

        productDeleteRequest = ProductDeleteRequest(cleanedElements.getProductNumber())
        foundProduct = self.__productRepository.findByProductNumber(productDeleteRequest.getProductNumber())

        if foundProduct is None:
            return ProductDeleteResponse(False)

        self.__productRepository.deleteByProductNumber(foundProduct.getProductNumber())
        return ProductDeleteResponse(True)