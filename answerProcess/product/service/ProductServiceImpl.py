from product.service.ProductService import ProductService
from product.service.request.ProductDeleteRequest import ProductDeleteRequest
from product.service.request.ProductUpdateRequest import ProductUpdateRequest
from product.service.request.ProductReadRequest import ProductReadRequest
from product.service.request.ProductRegisterRequest import ProductRegisterRequest
from product.service.response.ProductDeleteResponse import ProductDeleteResponse
from product.service.response.ProductListResponse import ProductListResponse
from product.service.response.ProductReadResponse import ProductReadResponse
from product.service.response.ProductRegisterResponse import ProductRegisterResponse
from product.service.response.ProductUpdateResponse import ProductUpdateResponse


class ProductServiceImpl(ProductService):
    __instance = None


    def __new__(cls, accountRepository, sessionRepository, productRepository, productOrderRepository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productRepository = productRepository
            cls.__instance.__accountRepository = accountRepository
            cls.__instance.__sessionRepository = sessionRepository
            cls.__instance.__productOrderRepository = productOrderRepository
        return cls.__instance

    @classmethod
    def getInstance(cls, accountRepository=None, sessionRepository=None,
                    productRepository=None, productOrderRepository=None):
        if cls.__instance is None:
            cls.__instance = cls(accountRepository,sessionRepository,productRepository, productOrderRepository)
        return cls.__instance

    def productRegister(self, *args, **kwargs):
        cleanedElements = args[0]
        seller = self.__accountRepository.findById(self.__sessionRepository.getIdBySessionId()).getAccountId()
        productRegisterRequest = ProductRegisterRequest(*cleanedElements)
        productRegisterRequest.setSeller(seller)

        registedProduct = self.__productRepository.save(productRegisterRequest.toProduct())
        if registedProduct is not None:
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

        else:
            return None


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
                foundProduct.getSeller(),
            )
            return productReadResponse
        else:
            print("상품을 찾을 수 없습니다.")
            return None

    def productList(self):
        print("productList 실행")
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
        print(f"productDelete 실행")
        cleanedElements = args[0]
        productDeleteRequest = ProductDeleteRequest(*cleanedElements)

        currentProductNumber = productDeleteRequest.getProductNumber()
        currentProductInfo = self.__productRepository.findProductByProductNumber(currentProductNumber)
        currentSeller = currentProductInfo.getSeller()
        accountId = self.__accountRepository.findById(self.__sessionRepository.getIdBySessionId()).getAccountId()

        if currentSeller == accountId:
            result = self.__productRepository.deleteProductByProductNumber(currentProductNumber)
            self.__productOrderRepository.removeAllProductsOrderByProductNumber(currentProductNumber)
            if result is True:
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
            else:
                return None

    def productUpdate(self, *args, **kwargs):
        print(f"productUpdate 실행")
        cleanedElements = args[0]
        productUpdateRequest = ProductUpdateRequest(*cleanedElements)

        currentProductNumber = productUpdateRequest.getProductNumber()
        currentProductInfo = self.__productRepository.findProductByProductNumber(currentProductNumber)
        currentSeller = currentProductInfo.getSeller()
        accountId = self.__accountRepository.findById(self.__sessionRepository.getIdBySessionId()).getAccountId()

        if currentSeller == accountId:
            result = self.__productRepository.updateProductInfo(productUpdateRequest)
            if result is True:
                foundProduct = self.__productRepository.findProductByProductNumber(
                    productUpdateRequest.getProductNumber())
                if foundProduct:
                    productUpdateResponse = ProductUpdateResponse(
                        productUpdateRequest.getProductNumber(),
                        foundProduct.getProductTitle(),
                        foundProduct.getProductPrice(),
                        foundProduct.getProductDetails(),
                        foundProduct.getSeller(),
                    )
                    return productUpdateResponse
                else:
                    print("상품을 찾을 수 없습니다.")
        return None