from sqlalchemy.orm import sessionmaker

from account.entity.Account import Account
from account.repository.AccountRepository import AccountRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError


class AccountRepositoryImpl(AccountRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # mysql 가져 오려면 아래와 같이 넣어야 함
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    def __init__(self):
        print("TaskManageRepository 생성자 호출")
        self.__receiverTask = None
        self.__transmitterTask = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def save(self, account):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            # commit 전 까지는 DB에 저장되지 않지만 commit 이후 DB에 저장됨
            session.add(account)
            session.commit()

            print(f"account - id: {account.getId()}")
            return account

        except SQLAlchemyError as exception:
            # error 발생 시 넣어 놨던 정보 rollback
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None

    def update(self, account):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        # 접근 제한자 (public, private 등) protected 키워드는 이런데서 사용됨
        # _Account__aacountId 와 account.getAccountId 가 같은지 비교하고 첫 번째 값을 가져와
        existingAccount = session.query(Account).filter_by(_Account__accountId=account.getAccountId()).first()
        if existingAccount:
            existingAccount.setPassword(account.getPassword())
            session.commit()

    def findById(self, id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Account).filter_by(_Account__id=id).first()

    def findByAccountId(self, accountId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        print(dir(Account))

        return session.query(Account).filter_by(_Account__accountId=accountId).first()

    def deleteByAccountId(self, accountId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        account = session.query(Account).filter_by(_Account__accountId=accountId).first()
        if account:
            session.delete(account)
            session.commit()

