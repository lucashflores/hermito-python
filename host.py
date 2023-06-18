from socket import *
from threading import *
from B8ZS import B8ZS
from VigenereCipher import VigenereCipher

PORT = 8080


class SocketServer():
    host: str
    server: socket
    thread: Thread
    data: list[str]

    def __init__(self) -> None:
        self.host = gethostbyname(gethostname())

    def get_host(self):
        return self.host

    def start_server(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, PORT))
        self.server.listen()
        self.thread = Thread(target=self.handleConnection)
        self.thread.start()

    def close_server(self):
        self.server.close()
        del self.thread
        del self.server

    def handleConnection(self):
        conn, address = self.server.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            message = conn.recv(2048).decode()
            print("from connected user: " + str(message))
            if message:
                print(f"[{address}] {message}")
                self.data = message
