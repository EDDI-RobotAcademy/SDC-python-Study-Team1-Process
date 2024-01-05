from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from mysql.MySQLDatabase import MySQLDatabase
from program.service.ProgramService import ProgramService
from program.service.response.ProgramQuitResponse import ProgramQuitResponse


class ProgramServiceImpl(ProgramService):
    __instance = None

    def __new__(cls, accountRepository, sessionRepository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = accountRepository
            cls.__instance.__sessionRepository = sessionRepository
        return cls.__instance

    @classmethod
    def getInstance(cls,accountRepository=None, sessionRepository=None):
        if cls.__instance is None:
            cls.__instance = cls(accountRepository, sessionRepository)
        return cls.__instance

    def programQuit(self):
        print("프로그램을 종료합니다.")
        try:
            self.__sessionRepository.resetSession()

            return ProgramQuitResponse(True)
        except Exception as e:
            print(f"exception: {e}")
            return ProgramQuitResponse(False)

