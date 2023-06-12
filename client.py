import socket
PORT = 8080


class SocketClient (socket):
    def __init__(self, host) -> None:
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, PORT))

    def send_message(self, message):
        self.sendall(message)
