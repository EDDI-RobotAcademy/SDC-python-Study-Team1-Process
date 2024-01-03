import ast

from account.service.request.AccountLoginRequest import AccountLoginRequest
from account.service.request.AccountRegisterRequest import AccountRegisterRequest
from account.service.response.AccountLoginResponse import AccountLoginResponse
from custom_protocol.entity.CustomProtocol import CustomProtocol
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
                CustomProtocol.PRODUCT_REGISTER.value] = cls.__instance.generateProductRegisterResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_READ.value] = cls.__instance.generateProductReadResponse


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
        if arguments is True:
            return False
        else:
            return True

    def generateAccountLoginResponse(self, arguments):
        print(f"ResponseGeneratorService: login sessionId: {arguments}")

        accountResponseData = {
            '__accountSessionId': arguments,
        }
        return accountResponseData

    def generateProductRegisterResponse(self, arguments):
        print("ProductRegisterResponse")
        if arguments is True:
            return True
        else:
            return False

    def generateProductReadResponse(self, arguments):
        print("ProductReadResponse")

        productResponseData = {
            '__productId': arguments['__productId'],
            '__productName': arguments['__productName'],
            '__productPrice': arguments['__productPrice'],
            '__productDetails': arguments['_productDetails'],
            '__seller': arguments['__seller']
        }

        return productResponseData

