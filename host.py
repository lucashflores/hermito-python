from socket import *
from threading import *
from B8ZS import B8ZS
from VigenereCipher import VigenereCipher

PORT = 8080

class SocketServer:
    host: str
    server: socket
    thread: Thread
    data: list[str]

    

    def __init__(self, callback) -> None:
        self.host = gethostbyname(gethostname())
        self.callback = callback

        self.text = ""
        self.message = ""
        self.binary = ""
        self.encrypted = ""

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
        key = "h189G%@A8AWFfbwahg!#"

        while True:
            self.message = conn.recv(2048).decode()
            if self.message:
                print(self.message)
                (self.encrypted, self.binary) = B8ZS.decode(self.message)
                print(self.encrypted)
                self.text = VigenereCipher.decrypt(self.encrypted, key)
                print(
                    f"[{address}]\nb8zs = {self.message} \nbinary = {self.binary} \nencrypted = {self.encrypted}\ntext = {self.text}\n\n"
                )
                self.data = f"[{address}] {self.message}"
                self.callback()
