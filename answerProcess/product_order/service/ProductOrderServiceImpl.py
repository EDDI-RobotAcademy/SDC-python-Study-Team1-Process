
from product_order.entity.ProductOrder import  ProductOrder
from product_order.service.ProductOrderService import ProductOrderService
from product_order.service.request.ProductOrderListRequest import ProductOrderListRequest
from product_order.service.request.ProductOrderReadRequest import ProductOrderReadRequest
from product_order.service.request.ProductOrderRegisterRequest import ProductOrderRegisterRequest
from product_order.service.request.ProductOrderRemoveRequest import ProductOrderRemoveRequest
from product_order.service.response.ProductOrderReadResponse import ProductOrderReadResponse
from product_order.service.response.ProductOrderRemoveResponse import ProductOrderRemoveResponse
from product_order.service.response.ProductOrderListResponse import ProductOrderListResponse
from product_order.service.response.ProductOrderRegisterResponse import ProductOrderRegisterResponse


class ProductOrderServiceImpl(ProductOrderService):
    __instance = None

    def __new__(cls, accountRepository, sessionRepository, productRepository, productOrderRepository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = accountRepository
            cls.__instance.__sessionRepository = sessionRepository
            cls.__instance.__productRepository = productRepository
            cls.__instance.__productOrderRepository = productOrderRepository
        return cls.__instance

    @classmethod
    def getInstance(cls, accountRepository=None, sessionRepository=None,
                    productRepository=None, productOrderRepository=None):
        if cls.__instance is None:
            cls.__instance = cls(accountRepository, sessionRepository, productRepository, productOrderRepository)
        return cls.__instance

    def orderList(self, *args, **kwargs):
        print("orderList()")

        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")

        productorderListRequest = ProductOrderListRequest(*cleanedElements)

        sessionId = productorderListRequest.getSessionId()
        productIdList = self.__productOrderRepository.findAllProductIdByAccountId(sessionId)
        print("productIdList: ", productIdList)
        orderList = []

        for order in productIdList:
            foundProduct = self.__productRepository.findProductByProductNumber(order)

            response = ProductOrderListResponse(
                foundProduct.getProductNumber(),
                foundProduct.getProductTitle(),
                foundProduct.getProductPrice()
            )
            orderList.append(dict(response))

        print(f"orderList: {orderList}")
        return orderList

    def orderRegister(self, *args, **kwargs):
        print("registerOrder 실행")

        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")


        productOrderRegisterRequest = ProductOrderRegisterRequest(*cleanedElements)
        print(f"type(productOrderRegisterRequest): {type(productOrderRegisterRequest)}")

        accountSessionId = productOrderRegisterRequest.getAccountId()
        productNumber = productOrderRegisterRequest.getProductNumber()
        if accountSessionId is None or productNumber is None:
            return ProductOrderRegisterResponse(False)
        order = ProductOrder(accountSessionId, productNumber)
        print(f"type(order): {type(order)}")

        self.__productOrderRepository.saveProductOrderInfo(order)

        if order:
            return ProductOrderRegisterResponse(True)
        else:
            return ProductOrderRegisterResponse(False)



    def orderRemove(self, *args, **kwargs):
        print("orderDelete()")

        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")

        productOrderRemoveRequest = ProductOrderRemoveRequest(*cleanedElements)

        accountSessionId = productOrderRemoveRequest.getAccountId()
        productNumber = productOrderRemoveRequest.getProductNumber()

        result = self.__productOrderRepository.removeProductsByAccountId(accountSessionId, productNumber)

        if result is True:
            return ProductOrderRemoveResponse(True)
        else:
            return ProductOrderRemoveResponse(False)


    def orderRead(self, *args, **kwargs):
        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")

        productOrderReadRequest = ProductOrderReadRequest(*cleanedElements)

        sessionId = productOrderReadRequest.getAccountSessionId()
        productNumber = productOrderReadRequest.getProductNumber()

        productList = self.__productOrderRepository.findAllProductIdByAccountId(sessionId)

        if productNumber in productList:
            foundProduct = self.__productRepository.findProductByProductNumber(productNumber)

            productReadResponse = ProductOrderReadResponse(
                productOrderReadRequest.getProductNumber(),
                foundProduct.getProductTitle(),
                foundProduct.getProductPrice(),
                foundProduct.getProductDetails(),
                foundProduct.getSeller(),
            )
            return productReadResponse
        else:
            print("상품을 찾을 수 없습니다.")
            return None



