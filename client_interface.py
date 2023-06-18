from tkinter import *
from client import SocketClient
from B8ZS import B8ZS
from VigenereCipher import VigenereCipher

class ClientInterface(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.client = SocketClient()
        self.connect_input = StringVar()
        self.message = StringVar()
        self.encrypted_message = StringVar(value="Mensagem Encriptada: ")
        self.binary_message = StringVar(value="Mensagem B8ZS:")
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.geometry("800x600")
        self.title("Client")

        self.title_label = Label(self, text="Cliente", font=("Arial", 30)).grid(column=0, row=0)
        self.label_text_input_connect = Label(self, text="IP do Host", font=(
            "arial", 12)).grid(column=0, row=1, sticky='W', padx=20)
        self.text_input_connect = Entry(self, textvariable=self.connect_input, font=('arial', 8, 'normal')).grid(
            row=2, column=0, sticky="WE", padx=20, pady=(0, 10))
        self.button_connect = Button(self, anchor="center", width=20, text="Conectar", font=(
            'calibre', 8, 'normal'), bd="2.5p", command=self.start_client).grid(
            row=3, column=0, sticky="WE", padx=20, pady=(0, 10))
        
        self.label_message = Label(self, text="Mensagem", font=(
            "arial", 12)).grid(column=0, row=4, sticky='W', padx=20)
        self.text_input_message = Entry(self, textvariable=self.message, font=('arial', 8, 'normal')).grid(
            row=5, column=0, sticky="WE", padx=20, pady=(0, 10))
        self.encrypted_message_label =  Label(self, textvariable=self.encrypted_message, font=(
            "arial", 12)).grid(column=0, row=6, sticky='W', padx=20)
        self.binary_message_label =  Text(self,height=5)
        self.binary_message_label.grid(column=0, row=7, sticky='W', padx=20)
        self.binary_message_label.insert(END,self.binary_message.get() )
        self.button_message = Button(self, anchor="center", width=20, text="Enviar Mensagem", font=(
            'calibre', 8, 'normal'), bd="2.5p", command=self.send_message).grid(
            row=8, column=0, sticky="WE", padx=20, pady=(0, 10))
        

    def start_client(self):
        self.client.start_client(self.connect_input.get())

    def send_message(self):
        key = "h189G%@A8AWFfbwahg!#"
        encrypted = VigenereCipher.encrypt(self.message.get(),key)
        self.encrypted_message.set(f"Mensagem Encriptada: {encrypted}")
        binary = B8ZS.encode(self.encrypted_message.get())
        self.binary_message.set(f"Mensagem B8ZS: {binary}")
        self.binary_message_label.delete("1.0", END)
        self.binary_message_label.insert(END,self.binary_message.get() )

            