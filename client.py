from socket import *
from B8ZS import B8ZS
from VigenereCipher import VigenereCipher
PORT = 8080


class SocketClient ():
    client: socket

    def __init__(self) -> None:
        self.client = socket(AF_INET, SOCK_STREAM)

    def start_client(self, host):
        self.client.connect((host, PORT))

    def send_message(self, message):
        encrypted_message = VigenereCipher.encrypt(message)
        self.client.send(B8ZS.encode(encrypted_message))

    def stop_client(self):
        self.client.close()
