from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from product.service.ProductService import ProductService
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.request.ProductDeleteRequest import ProductDeleteRequest
from product.service.request.ProductUpdateRequest import ProductUpdateRequest
# from product.service.request.ProductEditRequest import ProductEditRequest
from product.service.request.ProductReadRequest import ProductReadRequest
from product.service.request.ProductRegisterRequest import ProductRegisterRequest
from product.service.response.ProductDeleteResponse import ProductDeleteResponse
from product.service.response.ProductListResponse import ProductListResponse
# from product.service.response.ProductEditResponse import ProductEditResponse
from product.service.response.ProductReadResponse import ProductReadResponse
from product.service.response.ProductRegisterResponse import ProductRegisterResponse
from product.service.response.ProductUpdateResponse import ProductUpdateResponse


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls, productRepository, accountRepository, sessionRepository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productRepository = productRepository
            cls.__instance.__accountRepository = accountRepository
            cls.__instance.__sessionRepository = sessionRepository
        return cls.__instance


    @classmethod
    def getInstance(cls, productRepository=None, accountRepository=None, sessionRepository=None):
        if cls.__instance is None:
            cls.__instance = cls(productRepository, accountRepository, sessionRepository)
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
        print(f"productReadRequest: {productReadRequest}")

        foundProduct = self.__productRepository.findProductByProductNumber(productReadRequest.getProductNumber())
        print(f"foundProduct: {foundProduct}")

        if foundProduct:
            productReadResponse = ProductReadResponse(
                productReadRequest.getProductNumber(),
                foundProduct.getProductTitle(),
                foundProduct.getProductPrice(),
                foundProduct.getProductDetails(),
                foundProduct.getSeller(),
            )
            return productReadResponse
        else:
            print("상품을 찾을 수 없습니다.")
            return None

    def productList(self):
        productList = self.__productRepository.findAllProducts()
        list = []
        for Product in productList:
            response = ProductListResponse(
                Product.getProductNumber(),
                Product.getProductTitle(),
                Product.getProductPrice()
            )
            list.append(dict(response))
        return list


    def productDelete(self, *args, **kwargs):
        cleanedElements = args[0]

        productDeleteRequest = ProductDeleteRequest(*cleanedElements)
        foundProduct = self.__productRepository.findProductByProductNumber(productDeleteRequest.getProductNumber())

        if foundProduct is None:
            return ProductDeleteResponse(False)

        self.__productRepository.deleteProductByProductNumber(foundProduct.getProductNumber())
        return ProductDeleteResponse(True)

    def productUpdate(self, *args, **kwargs):
        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")

        productUpdateRequest = ProductUpdateRequest(cleanedElements.getProductTitle(), cleanedElements.getProductDetails(),
                                                    cleanedElements.getSeller(), cleanedElements.getProductPrice())
        print(productUpdateRequest)

        # data = self.__productRepository.save(productUpdateRequest.toProduct())
        foundProduct = self.__productRepository.findProductByProductNumber(productUpdateRequest.getProductNumber())
        print(type[foundProduct])

        if foundProduct is not None:
            foundProduct.setProductName(productUpdateRequest.getProductTitle())
            foundProduct.setDescription(productUpdateRequest.getProductDetails())
            foundProduct.setSeller(productUpdateRequest.getSeller())
            foundProduct.setPrice(productUpdateRequest.getProductPrice())

            savedProduct = self.__productRepository.save(foundProduct)
            print(f"foundProduct: {foundProduct}")
            print(f"savedProduct: {savedProduct}")

            return ProductUpdateResponse(
                savedProduct.getProductNumber(),
                savedProduct.getProductTitle(),
                savedProduct.getProductDetails(),
                savedProduct.getSeller(),
                savedProduct.getProductPrice(),
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
