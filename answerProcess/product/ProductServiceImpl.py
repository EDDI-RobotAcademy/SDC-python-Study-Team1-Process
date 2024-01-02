from account.entity.Account import Account
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
        print("TaskManageServiceImpl 생성자 호출")
        self.__productRepository = ProductRepositoryImpl()

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def registerProduct(self, *args, **kwargs):
        cleanedElements = args[0]

        productRegisterRequest = ProductRegisterRequest(cleanedElements.getProductName(),
                                                        cleanedElements.getDescription(),
                                                        cleanedElements.getSeller(), cleanedElements.getPrice())
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

    def updateProduct(self, *args, **kwargs):
        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")

        productUpdateRequest = ProductUpdateRequest(cleanedElements.getProductName(), cleanedElements.getDescription(),
                                                    cleanedElements.getSeller(), cleanedElements.getPrice())
        print(productUpdateRequest)

        # data = self.__productRepository.save(productUpdateRequest.toProduct())
        foundProduct = self.__productRepository.findByProductNumber(productUpdateRequest.getProductNumber())
        print(type[foundProduct])

        if foundProduct is not None:
            foundProduct.setProductName(productUpdateRequest.getProductName())
            foundProduct.setDescription(productUpdateRequest.getDescription())
            foundProduct.setSeller(productUpdateRequest.getSeller())
            foundProduct.setPrice(productUpdateRequest.getPrice())

            savedProduct = self.__productRepository.save(foundProduct)
            print(f"foundProduct: {foundProduct}")
            print(f"savedProduct: {savedProduct}")

            return ProductUpdateResponse(
                savedProduct.getProductNumber(),
                savedProduct.getProductName(),
                savedProduct.getDescription(),
                savedProduct.getSeller(),
                savedProduct.getPrice(),
            )

        return None

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
