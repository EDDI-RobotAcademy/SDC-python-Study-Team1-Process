from account.entity.Account import Account
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from product.ProductService import ProductService
from product.entity.Product import Product
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.request.ProductDeleteRequest import ProductDeleteRequest
from product.service.request.ProductUpdateRequest import ProductUpdateRequest
# from product.service.request.ProductEditRequest import ProductEditRequest
from product.service.request.ProductReadRequest import ProductReadRequest
from product.service.request.ProductRegisterRequest import ProductRegisterRequest
from product.service.response import ProductListResponse
from product.service.response.ProductDeleteResponse import ProductDeleteResponse
# from product.service.response.ProductEditResponse import ProductEditResponse
from product.service.response.ProductReadResponse import ProductReadResponse
from product.service.response.ProductRegisterResponse import ProductRegisterResponse
from product.service.response.ProductUpdateResponse import ProductUpdateResponse


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

    def productRegister(self, *args, **kwargs):
        cleanedElements = args[0]
        seller = self.__accountRepository.findById(self.__sessionRepository.getIdBySessionId()).getAccountId()
        productRegisterRequest = ProductRegisterRequest(*cleanedElements)
        productRegisterRequest.setSeller(seller)

        registedProduct = self.__productRepository.save(productRegisterRequest.toProduct())
        if registedProduct is not None:
            return ProductRegisterResponse(True)
        else:
            return ProductRegisterResponse(False)


    def productRead(self, *args, **kwargs):
        cleanedElements = args[0]

        productReadRequest = ProductReadRequest(*cleanedElements)

        foundProduct = self.__productRepository.findProductByProductNumber(productReadRequest.getProductNumber())

        if foundProduct:
            productReadResponse = ProductReadResponse(
                productReadRequest.getProductNumber(),
                foundProduct.getProductTitle(),
                foundProduct.getProductPrice(),
                foundProduct.getProductDetails(),
                foundProduct.getSeller()
            )
            return productReadResponse
        else:
            print("상품을 찾을 수 없습니다.")
            return None

    def productList(self):
        productList = self.__productRepository.findAllProducts()
        return productList

    def productDelete(self, *args, **kwargs):
        cleanedElements = args[0]
        productDeleteRequest = ProductDeleteRequest(cleanedElements.getProductNumber())
        repository = ProductRepositoryImpl.getInstance()
        result = repository.deleteProductByProductNumber(productDeleteRequest)
        return result

    def productUpdate(self, *args, **kwargs):
        cleanedElements = args[0]
        productUpdateRequest = ProductUpdateRequest(cleanedElements.getProductNumber(),
                                                    cleanedElements.getProductTitle(),
                                                    cleanedElements.getProductDetails(),
                                                    cleanedElements.getProductPrice())
        result = self.__productRepository.updateProductInfo(productUpdateRequest)
        if result == True:
            return self.__productRepository.findProductByProductNumber(cleanedElements.getProductNumber())


    # def productUpdate(self, *args, **kwargs):
    #     cleanedElements = args[0]
    #     productUpdateRequest = ProductUpdateRequest(*cleanedElements)
    #     response = self.repository(productUpdateRequest)
    #     return response
    #
    # def updateProduct(self, *args, **kwargs):
    #     cleaned_elements = args[0]
    #     product_update_request = ProductUpdateRequest(*cleaned_elements)
    #
    #     saved_product = self.repository.updateProductInfo(product_update_request.toProduct())
    #     return ProductUpdateResponse(
    #             saved_product.getProductNumber(),
    #             saved_product.getProductName(),
    #             saved_product.getDescription(),
    #             saved_product.getPrice(),
    #         )
