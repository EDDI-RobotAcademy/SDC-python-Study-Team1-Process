import ast

from account.service.request.AccountDeleteRequest import AccountDeleteRequest
from account.service.request.AccountLoginRequest import AccountLoginRequest
from account.service.request.AccountRegisterRequest import AccountRegisterRequest
from account.service.request.AccountLogoutRequest import AccountLogoutRequest
from custom_protocol.entity.CustomProtocol import CustomProtocol
from product.service.request.ProductDeleteRequest import ProductDeleteRequest
from product.service.request.ProductReadRequest import ProductReadRequest
from product.service.request.ProductRegisterRequest import ProductRegisterRequest
from product.service.request.ProductUpdateRequest import ProductUpdateRequest
from product_order.service.request.ProductOrderListRequest import ProductOrderListRequest
from product_order.service.request.ProductOrderRegisterRequest import ProductOrderRegisterRequest
from request_generator.service.RequestGeneratorService import RequestGeneratorService


class RequestGeneratorServiceImpl(RequestGeneratorService):
    __instance = None
    __requestFormGenerationTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_REGISTER.value] = cls.__instance.generateAccountRegisterRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGIN.value] = cls.__instance.generateAccountLoginRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGOUT.value] = cls.__instance.generateAccountLogoutRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_REMOVE.value] = cls.__instance.generateAccountDeleteRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_REGISTER.value] = cls.__instance.generateProductRegisterRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_READ.value] = cls.__instance.generateProductReadRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_MODIFY.value] = cls.__instance.generateProductModifyRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_PURCHASE.value] = cls.__instance.generateProductPurchaseRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_REMOVE.value] = cls.__instance.generateProductRemoveRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ORDER_LIST.value] = cls.__instance.generateProductOrderListRequest

        return cls.__instance

    def __init__(self):
        print("RequestGeneratorServiceImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findRequestGenerator(self, protocolNumber):
        print("request generator를 찾아옵니다")
        if self.__requestFormGenerationTable[protocolNumber] is not None:
            return self.__requestFormGenerationTable[protocolNumber]

        else:
            print(f"이 프로토콜 번호({protocolNumber}) 를 처리 할 수 있는 함수가 없습니다.")

    def generateAccountRegisterRequest(self, arguments):
        print("AccountRegisterRequest 생성")
        return AccountRegisterRequest(
            __accountId=arguments["__accountId"],
            __password=arguments["__password"]
        )

    def generateAccountLoginRequest(self, arguments):
        print("AccountLoginRequest 생성")
        return AccountLoginRequest(
            __accountId=arguments["__accountId"],
            __password=arguments["__password"]
        )

    def generateAccountDeleteRequest(self, arguments):
        print("AccountDeleteRequest 생성")
        return AccountDeleteRequest(
            __accountSessionId=arguments["__accountSessionId"]
        )

    def generateAccountLogoutRequest(self, arguments):
        print("AccountLogoutRequest 생성")
        return AccountLogoutRequest(
            __accountSessionId=arguments["__accountSessionId"]
        )

    def generateProductRegisterRequest(self, arguments):
        print("ProductRegisterRequest 생성")
        return ProductRegisterRequest(
            __productTitle=arguments["__productTitle"],
            __productDetails=arguments["__productDetails"],
            __productPrice=arguments["__productPrice"]
        )

    def generateProductReadRequest(self, arguments):
        print("ProductReadRequest 생성")
        return ProductReadRequest(
            __productNumber=arguments["__productNumber"]
        )

    def generateProductModifyRequest(self, arguments):
        print("ProductModifyRequest 생성")
        return ProductUpdateRequest(
            __productNumber=arguments['__productNumber'],
            __productTitle=arguments['__productTitle'],
            __productDetails=arguments['__productDetails'],
            __productPrice=arguments['__productPrice']
        )

    def generateProductPurchaseRequest(self, arguments):
        print("ProductPurchaseRequest 생성")
        return ProductOrderRegisterRequest(
            __productNumber=arguments["__productNumber"],
            __accountSessionId=arguments["__accountSessionId"]
        )

    def generateProductRemoveRequest(self, arguments):
        print("ProductRemoveRequest 생성")
        return ProductDeleteRequest(
            __productNumber=arguments["__productNumber"]
        )

    def generateProductOrderListRequest(self, arguments):
        print("ProductOrderListRequest 생성")
        return ProductOrderListRequest(
            __accountSessionId=arguments["__accountSessionId"]
        )

