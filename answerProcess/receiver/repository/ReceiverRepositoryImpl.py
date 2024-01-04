import errno
import json
from socket import socket
from time import sleep

from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from receiver.repository.ReceiverRepository import ReceiverRepository
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from response_generator.service.ResponseGeneratorServiceImpl import ResponseGeneratorServiceImpl
from transmitter.repository.TransmitterRepositoryImpl import TransmitterRepositoryImpl

import re


class ReceiverRepositoryImpl(ReceiverRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ReceiverRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def receiveCommand(self, clientSocket):
        transmitterRepository = TransmitterRepositoryImpl.getInstance()
        transmitQueue = transmitterRepository.getTransmitQueue()

        customProtocolRepository = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        while True:
            try:
                receivedRequest = clientSocket.recv(1024)

                if not receivedRequest:
                    clientSocket.closeSocket()
                    break

                receivedForm  = json.loads(receivedRequest)
                protocolNumber = receivedForm["protocol"]
                print(f"typeof protocolNumber: {type(protocolNumber)}")
                print(f"protocolNumber: {protocolNumber}")

                if "data" in receivedForm:
                    receivedRequestForm = receivedForm["data"]
                    print(f"typeof requestForm: {type(receivedRequestForm)}")
                    print(f"requestForm: {receivedRequestForm}")
                    requestGenerator = requestGeneratorService.findRequestGenerator(protocolNumber)
                    requestForm = requestGenerator(receivedRequestForm)

                    response = customProtocolRepository.execute(int(protocolNumber), tuple(requestForm.__dict__.values()))
                    print(f"response: {response}")
                else:
                    response = customProtocolRepository.execute(int(protocolNumber))
                    print(f"response: {response}")

                responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()

                responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber)
                responseForm = responseGenerator(response)

                combinedResponse = {
                    'protocol': protocolNumber,
                    'data': responseForm
                }

                transmitQueue.put(combinedResponse)

            except socket.error as exception:
                if exception.errno == errno.EWOULDBLOCK:
                    pass

            finally:
                sleep(0.5)


