from account.entity.Account import Account
from product.ProductService import ProductService
from product.entity.Product import Product
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.request.ProductDeleteRequest import ProductDeleteRequest
from product.service.request.ProductReadRequest import ProductReadRequest
from product.service.request.ProductRegisterRequest import ProductRegisterRequest
from product.service.response import ProductListResponse
from product.service.response.ProductDeleteResponse import ProductDeleteResponse
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
        print("TaskManageServiceImpl 생성자 호출")
        self.__productRepository = ProductRepositoryImpl()

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def registerProduct(self, *args, **kwargs):
        cleanedElements = args[0]

        productRegisterRequest = ProductRegisterRequest(cleanedElements.getProductName(), cleanedElements.getDescription(), cleanedElements.getSeller(), cleanedElements.getPrice())
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

            # print(f"상품 이름: {data.getProductName()}")
            # print(f"상품 설명: {data.getDescription()}")
            # print(f"판매자: {data.getSeller()}")
            # print(f"상품 가격: {data.getPrice()}")

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