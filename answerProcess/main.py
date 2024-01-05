import multiprocessing
import socket
from time import sleep

from account.repository.AccountRepository import AccountRepository
from account.repository.AccountRepositoryImpl import AccountRepositoryImpl
from account.repository.SessionRepositoryImpl import SessionRepositoryImpl
from account.service.AccountServiceImpl import AccountServiceImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.service.CustomProtocolServiceImpl import CustomProtocolServiceImpl
from mysql.MySQLDatabase import MySQLDatabase
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.ProductServiceImpl import ProductServiceImpl
from product_order.repository.ProductOrderRepositoryImpl import ProductOrderRepositoryImpl
from product_order.service.ProductOrderService import ProductOrderService
from product_order.service.ProductOrderServiceImpl import ProductOrderServiceImpl
from server_socket.repository.ServerSocketRepositoryImpl import ServerSocketRepositoryImpl
from server_socket.service.ServerSocketServiceImpl import ServerSocketServiceImpl
from task_manage.repository.TaskManageRepositoryImpl import TaskManageRepositoryImpl
from task_manage.service.TaskManageServiceImpl import TaskManageServiceImpl
from utility.IPAddressBindSupporter import IPAddressBindSupporter
from mysql.MySQLProcess import DbProcess
# pip3 install pymysql

# pip3 install sqlalchemy
# pip3 install mysql-connector-python
from decouple import config

MYHOST = IPAddressBindSupporter.getIpAddressFromGoogle()

# query form 을 항상 생각해서 넣었어야 하지만
# 밑에 Alternatives 를 사용함으로 아무거나 넣도 다 처리
def initMysqlInstance():
    dbInstance = DbProcess(
        host=config('HOST'),
        user=config('DB_USER'),
        password=config('PASSWORD'),
        database=config('DATABASE')
    )
    dbInstance.connect()


def initMysqlInstanceAlternatives():
    mysqlDatabase = MySQLDatabase.getInstance()
    mysqlDatabase.connect()


def initServerSocketDomain():
    serverSocketRepository = ServerSocketRepositoryImpl()
    ServerSocketServiceImpl(serverSocketRepository)


def initTaskManageDomain():
    taskManageRepository = TaskManageRepositoryImpl()
    TaskManageServiceImpl(taskManageRepository)


def initCustomProtocol():
    customProtocolService = CustomProtocolServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    productService = ProductServiceImpl.getInstance()
    productOrderService = ProductOrderServiceImpl.getInstance()

    print(f"enum value test: {CustomProtocol.ACCOUNT_REGISTER.value}")
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_REGISTER.value,
        accountService.registerAccount
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_LOGIN.value,
        accountService.loginAccount
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_LOGOUT.value,
        accountService.logoutAccount
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_REMOVE.value,
        accountService.deleteAccount
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_LIST.value,
        productService.productList
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_REGISTER.value,
        productService.productRegister
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_READ.value,
        productService.productRead
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_MODIFY.value,
        productService.productUpdate
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_PURCHASE.value,
        productOrderService.orderRegister
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_REMOVE.value,
        productService.productDelete
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_LIST.value,
        productOrderService.orderList
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_REMOVE.value,
        productOrderService.orderRemove
    )


def initAccountDomain():
    accountRepository = AccountRepositoryImpl()
    sessionRepository = SessionRepositoryImpl()
    AccountServiceImpl(accountRepository, sessionRepository)


def initProductDomain():
    accountRepository = AccountRepositoryImpl.getInstance()
    sessionRepository = SessionRepositoryImpl.getInstance()
    productRepository = ProductRepositoryImpl()
    ProductServiceImpl(accountRepository, sessionRepository, productRepository)


def initOrderDomain():
    accountRepository = AccountRepositoryImpl.getInstance()
    sessionRepository = SessionRepositoryImpl.getInstance()
    productRepository = ProductRepositoryImpl.getInstance()
    productOrderRepository = ProductOrderRepositoryImpl.getInstance()
    ProductOrderServiceImpl(accountRepository, sessionRepository, productRepository, productOrderRepository)


def initEachDomain():
    # initMysqlInstance()
    initMysqlInstanceAlternatives()

    initAccountDomain()
    initProductDomain()
    initOrderDomain()

    initServerSocketDomain()
    initTaskManageDomain()
    initCustomProtocol()


if __name__ == '__main__':
    print(f"ip: {IPAddressBindSupporter.getIpAddress()}")
    print(f"ip: {IPAddressBindSupporter.getLocalIPAddress()}")
    print(f"ip: {IPAddressBindSupporter.getIpAddressFromGoogle()}")

    initEachDomain()

    serverSocketService = ServerSocketServiceImpl.getInstance()

    serverSocketService.createServerSocket(MYHOST, int(config('PORT')))
    serverSocketService.setSocketOption(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    serverSocketService.bindServerSocket()
    serverSocketService.setServerListenNumber(15)
    serverSocketService.setBlockingOperation()

    # taskManageService = TaskManageServiceImpl.getInstance()

    queue = multiprocessing.Queue()

    while True:
        try:
            serverSocketService.acceptClientSocket(queue)

            # if not queue.empty():
            #     print("main: 사용자가 접속했습니다!")
            #     taskManageService.createReceiveTask()
            #     taskManageService.createTransmitTask()

        except socket.error:
            sleep(1.0)


# 보편적으로 서비스를 제공하는 입장에 놓여 있으면 Server(서버)
# 서비스를 받는 입장에 있으면 Client(클라이언트) 라고 합니다.
# 앞으로 만들 UI는 현재 작성한 Server에게 요청(Request)를 합니다.
# 그럼 UI는 Server가 준 응답(Response)를 가지고 지 나름대로의 기준으로 처리를 합니다.
