
from product_order.entity.ProductOrder import  ProductOrder
from product_order.service.ProductOrderService import ProductOrderService
from product_order.service.request.ProductOrderListRequest import ProductOrderListRequest
from product_order.service.request.ProductOrderRegisterRequest import ProductOrderRegisterRequest
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
        orderByAccountList = self.__productOrderRepository.findAllProductIdByAccountId(sessionId)

        orderList = []

        for order in orderByAccountList:
            productId = order.getProductId()
            foundProduct = self.__productRepository.findById(productId)

            orderList.append({
                'productName': foundProduct.getName(),
                'price': foundProduct.getPrice(),
            })

        print(f"orderList: {orderList}")

        orderListResponse = ProductOrderListResponse(orderList)
        print(f"orderListResponse: {orderListResponse}")

        return ProductOrderListResponse.toDict()

    def orderRegister(self, *args, **kwargs):
        print("registerOrder()")

        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")

        if cleanedElements.getSessionId() == -1:
            response = ProductOrderRegisterResponse(False)
            return response

        else:
            productorderRegisterRequest = ProductOrderRegisterRequest(*cleanedElements)

            sessionId = productorderRegisterRequest.getAccountId()
            productId = productorderRegisterRequest.getProductNumber()
            order = ProductOrder(sessionId, productId)

            self.__productOrderRepository.saveProductOrderInfo(order)

            if order:
                response = ProductOrderRegisterResponse(True)
            else:
                response = ProductOrderRegisterResponse(False)
            return response



    def orderDelete(self, *args, **kwargs):
        print("orderDelete()")

        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")



