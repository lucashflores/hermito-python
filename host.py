from socket import *
PORT = 8080


class SocketServer():
    host: str
    server: socket

    def __init__(self) -> None:
        self.host = gethostbyname(gethostname())
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, PORT))

    def get_host(self):
        return self.host

    def start_server(self):
        self.server.listen()

    def close_server(self):
        self.server.close()
