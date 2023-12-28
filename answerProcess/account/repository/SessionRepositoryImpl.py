from sqlalchemy.orm import sessionmaker
from account.entity.Session import Session
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


    def save(self, acountSession: Session):
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


    def findById(self, id):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        return session.query(Session).filter_by(_Session__Id=id).first()

    def findBySessionId(self, sessionId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()

        print(dir(Session))

        return session.query(Session).filter_by(_Session__sessionId=sessionId).first()

    def deleteBySessionId(self, sessionId):
        dbSession = sessionmaker(bind=self.__instance.engine)
        session = dbSession()
        print("세션")

        acountSession = session.query(Session).filter_by(_Session__sessionId=sessionId).first()
        print("해당 아이디정보 찾는")
        if acountSession:
            session.delete(acountSession)
            session.commit()