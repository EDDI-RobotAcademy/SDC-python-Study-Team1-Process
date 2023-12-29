from session.entity.Session import Session
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from session.repository.SessionRepositoryImpl import SessionRepositoryImpl
from account.service.AccountService import AccountService
from account.service.request.AccountLoginRequest import AccountLoginRequest
from account.service.request.AccountRegisterRequest import AccountRegisterRequest
from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountRegisterResponse import AccountRegisterResponse
from account.service.request.AccountDeleteRequest import AccountDeleteRequest
from account.service.response.AccountDeleteResponse import AccountDeleteResponse


class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repository = repository
        return cls.__instance

    def __init__(self, repository):
        print("AccountRepositoryImpl 생성자 호출")
        self.__accountRepository = AccountRepositoryImpl()
        self.__sessionRepository = SessionRepositoryImpl()

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def registerAccount(self, *args, **kwargs):
        print("registerAccount()")
        print(f"args: {args}")
        cleanedElements = args[0]
        print(f"cleanedElements: {cleanedElements}")

        accountRegisterRequest = AccountRegisterRequest(*cleanedElements)
        storedAccount = self.__accountRepository.save(accountRegisterRequest.toAccount())

        if storedAccount.getId() is not None:
            return AccountRegisterResponse(True)
        return AccountRegisterResponse(False)




    def deleteAccount(self, *args, **kwargs):
        print("AccountService - deleteAccount()")

        cleanedElements = args[0]

        accountLoginRequest = AccountDeleteRequest(*cleanedElements)
        foundAccount = self.__accountRepository.findById(accountLoginRequest.getAccountSessionId())
        print(f"foundAccount: {foundAccount}")
        if foundAccount is None:
            return AccountDeleteResponse(False)

        self.__sessionRepository.deleteBySessionId(foundAccount.getId())
        self.__accountRepository.deleteById(foundAccount.getId())

        return AccountDeleteResponse(True)

    def loginAccount(self, *args, **kwargs):
        cleanedElements = args[0]

        print(f"cleanedElements: {cleanedElements}")

        accountLoginRequest = AccountLoginRequest(*cleanedElements)

        if self.__accountRepository.getBoolWithFindByAccountId(accountLoginRequest.getAccountId()) is True:
            print("아이디 일치")
            databaseAccount = self.__accountRepository.findByAccountId(cleanedElements[0])
            if databaseAccount.checkPassword(accountLoginRequest.getPassword()) is True:
                print("비밀번호 일치")
                accountsession = Session(databaseAccount.getId())
                self.__sessionRepository.save(accountsession)
                return AccountLoginResponse(databaseAccount.getId())
        
        print("비밀번호 불일치")
        return None

