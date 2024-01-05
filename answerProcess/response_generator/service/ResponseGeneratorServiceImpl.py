import ast

from account.service.response.AccountRegisterResponse import AccountRegisterResponse
from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountDeleteResponse import AccountDeleteResponse
from account.service.response.AccountLogoutResponse import AccountLogoutResponse
from custom_protocol.entity.CustomProtocol import CustomProtocol
from product.service.response.ProductReadResponse import ProductReadResponse
from request_generator.service.RequestGeneratorService import RequestGeneratorService
from response_generator.service.ResponseGeneratorService import ResponseGeneratorService


class ResponseGeneratorServiceImpl(ResponseGeneratorService):
    __instance = None
    __responseFormGenerationTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_REGISTER.value] = cls.__instance.generateAccountRegisterResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGIN.value] = cls.__instance.generateAccountLoginResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_REMOVE.value] = cls.__instance.generateAccountDeleteResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGOUT.value] = cls.__instance.generateAccountLogoutResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_LIST.value] = cls.__instance.generateProductListResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_REGISTER.value] = cls.__instance.generateProductRegisterResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_READ.value] = cls.__instance.generateProductReadResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_MODIFY.value] = cls.__instance.generateProductUpdateResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_PURCHASE.value] = cls.__instance.generateProductOrderRegisterResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_REMOVE.value] = cls.__instance.generateProductRemoveResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ORDER_LIST.value] = cls.__instance.generateProductOrderListResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ORDER_READ.value] = cls.__instance.generateProductOrderReadResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ORDER_REMOVE.value] = cls.__instance.generateProductOrderRemoveResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.EXIT.value] = cls.__instance.generateProgramQuitResponse


        return cls.__instance

    def __init__(self):
        print("ResponseGeneratorServiceImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findResponseGenerator(self, protocolNumber):
        print("response generator를 찾아옵니다")
        if self.__responseFormGenerationTable[protocolNumber] is not None:
            return self.__responseFormGenerationTable[protocolNumber]

        else:
            print(f"이 프로토콜 번호({protocolNumber}) 를 처리 할 수 있는 함수가 없습니다.")

    def generateAccountRegisterResponse(self, arguments):
        print("AccountRegisterResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateAccountLoginResponse(self, arguments):
        print(f"ResponseGeneratorService: login sessionId: {arguments}")

        accountResponseData = {
            '__accountSessionId': arguments,
        }

        return accountResponseData

    def generateAccountDeleteResponse(self, arguments):
        print("AccountDeleteResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateAccountLogoutResponse(self, arguments):
        print("AccountLogoutResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateProductListResponse(self, arguments):
        print("ProductListResponse 생성")
        return arguments

    def generateProductRegisterResponse(self, arguments):
        print("ProductRegisterResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateProductUpdateResponse(self, arguments):
        print("ProductUpdateResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateProductReadResponse(self, arguments):
        print("ProductReadResponse 생성")
        if arguments is None:
            productResponseData = {
            '__productNumber': None,
            '__productTitle': None,
            '__productPrice': None,
            '__productDetails': None,
            '__seller': None
            }
            return productResponseData
        print(f"arguments: {arguments}")
        resutl = dict(arguments)

        productResponseData = {
            '__productNumber': resutl['__productNumber'],
            '__productTitle': resutl['__productTitle'],
            '__productPrice': resutl['__productPrice'],
            '__productDetails': resutl['__productDetails'],
            '__seller': resutl['__seller']
        }
        return productResponseData

    def generateProductOrderRegisterResponse(self, arguments):
        print("ProductOrderRegisterResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateProductRemoveResponse(self, arguments):
        print("ProductRemoveResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateProductOrderListResponse(self, arguments):
        print("ProductOrderListResponse 생성")
        return arguments

    def generateProductOrderReadResponse(self, arguments):
        print("ProductOrderReadResponse 생성")
        if arguments is None:
            productOrderResponseData = {
                '__productNumber': None,
                '__productTitle': None,
                '__productPrice': None,
                '__productDetails': None,
                '__seller': None
            }
            return productOrderResponseData
        print(f"arguments: {arguments}")
        resutl = dict(arguments)

        productOrderResponseData = {
            '__productNumber': resutl['__productNumber'],
            '__productTitle': resutl['__productTitle'],
            '__productPrice': resutl['__productPrice'],
            '__productDetails': resutl['__productDetails'],
            '__seller': resutl['__seller']
        }
        return productOrderResponseData

    def generateProductOrderRemoveResponse(self, arguments):
        print("ProductOrderRemoveResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False

    def generateProgramQuitResponse(self, arguments):
        print("ProgramQuitResponse 생성")
        if arguments.getIsSuccess() is True:
            return True
        else:
            return False



