from sqlalchemy.orm import sessionmaker
from account.entity.AccountSession import AccountSession
from account.repository.SessionRepository import SessionRepository
from mysql.MySQLDatabase import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError


class SessionRepositoryImpl(SessionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.engine = MySQLDatabase.getInstance().getMySQLEngine()
        return cls.__instance

    def __init__(self):
        print("SessionRepositoryImpl 생성자 호출")
        self.__receiverTask = None
        self.__transmitterTask = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


    def save(self, acountSession: AccountSession):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        try:
            session.add(acountSession)
            session.commit()

            print(f"account - id: {acountSession.getSessionId()}")
            return acountSession

        except SQLAlchemyError as exception:
            session.rollback()
            print(f"DB 저장 중 에러 발생: {exception}")
            return None


    def getIdBySessionId(self):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        sessionlist = session.query(AccountSession).all()
        targetsessionId = sessionlist[0]
        sessionId = targetsessionId.getSessionId()
        return sessionId

    def deleteBySessionId(self, sessionId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        print("세션")

        acountSession = session.query(AccountSession).filter_by(_AccountSession__sessionId=sessionId).first()
        print("해당 아이디정보 찾는")
        if acountSession:
            session.delete(acountSession)
            session.commit()


    def resetSession(self):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        print("세션")

        acountSession = session.query(AccountSession).all()
        for session_obj in acountSession:
            session.delete(session_obj)
        session.commit()
        print("AccountSession객체 초기화")

