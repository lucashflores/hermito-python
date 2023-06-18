from socket import *
PORT = 8080


class SocketClient ():
    client: socket

    def __init__(self) -> None:
        self.client = socket(AF_INET, SOCK_STREAM)
    
    def start_client(self, host): 
        self.client.connect((host, PORT))

    def send_message(self, message):
        self.client.sendall(message)

    def stop_client(self):
        self.client.close()
