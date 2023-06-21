from tkinter import *
from client import SocketClient
from B8ZS import B8ZS
from VigenereCipher import VigenereCipher
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ClientInterface(Toplevel):
    def __init__(self, root):
        super().__init__(root)

        self.client = SocketClient()

        self.connect_input = StringVar()
        self.message = StringVar()
        self.encrypted_message = StringVar()
        self.b8zs_message = StringVar()

        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.geometry("1024x600")

        self.label_text_input_connect = Label(
            self, text="IP do Host", font=("arial", 12)
        )
        self.label_text_input_connect.grid(column=0, row=1, sticky="W", padx=20)

        self.text_input_connect = Entry(
            self, textvariable=self.connect_input, font=("arial", 8, "normal")
        )
        self.text_input_connect.grid(
            row=2, column=0, sticky="WE", padx=20, pady=(0, 10)
        )

        self.button_connect = Button(
            self,
            anchor="center",
            width=20,
            text="Conectar",
            font=("calibre", 8, "normal"),
            bd="2.5p",
            command=self.start_client,
        )
        self.button_connect.grid(row=3, column=0, sticky="WE", padx=20, pady=(0, 10))

        self.label_message = Label(self, text="Mensagem", font=("arial", 12))
        self.label_message.grid(column=0, row=4, sticky="W", padx=20)

        self.text_input_message = Entry(
            self, textvariable=self.message, font=("arial", 8, "normal")
        )
        self.text_input_message.grid(
            row=5, column=0, sticky="WE", padx=20, pady=(0, 10)
        )

        self.encrypted_message_label = Label(
            self, text="Mensagem Encriptada: ", font=("arial", 12)
        )
        self.encrypted_message_label.grid(column=0, row=6, sticky="W", padx=20)

        self.encrypted_message_text = Text(self, height=1, width=160)
        self.encrypted_message_text.grid(column=0, row=7, sticky="W", padx=20)
        self.encrypted_message_text.insert(END, self.encrypted_message.get())

        self.binary_message_label = Label(self, text="Mensagem Binária: ", font=("arial", 12))
        self.binary_message_label.grid(column=0, row=8, sticky="W", padx=20)

        self.binary_message_text = Text(self, height=5, width=160, font=("arial", 10))
        self.binary_message_text.grid(column=0, row=9, sticky="W", padx=20)
        #self.binary_message_text.insert(END, self.binary_message.get()) ???????

        self.b8zs_message_label = Label(self, text="B8ZS: ", font=("arial", 12))
        self.b8zs_message_label.grid(column=0, row=10, sticky="W", padx=20)

        self.b8zs_message_text = Text(self, height=5, width=160, font=("arial", 10))
        self.b8zs_message_text.grid(column=0, row=11, sticky="W", padx=20)
        self.b8zs_message_text.insert(END, self.b8zs_message.get())

        self.button_message = Button(
            self,
            anchor="center",
            width=20,
            text="Enviar Mensagem",
            font=("calibre", 8, "normal"),
            bd="2.5p",
            command=self.send_message,
        )
        self.button_message.grid(row=12, column=0, sticky="WE", padx=20, pady=(0, 10))

    def start_client(self):
        self.client.start_client(self.connect_input.get())

    def send_message(self):
        key = "h189G%@A8AWFfbwahg!#"
        self.update_display(key)
        self.client.send_message(self.message.get(), key)

    def update_display(self, key: str):
        encrypted = VigenereCipher.encrypt(self.message.get(), key)

        self.encrypted_message.set(encrypted)
        self.encrypted_message_text.delete("1.0", END)
        self.encrypted_message_text.insert(END, self.encrypted_message.get())

        binary = B8ZS.encode(self.encrypted_message.get())

        self.b8zs_message.set(binary)
        self.b8zs_message_text.delete("1.0", END)
        self.b8zs_message_text.insert(END, self.b8zs_message.get())

        self.plot_graph(binary)

    def plot_graph(self, binary):
        fig, ax = plt.subplots()
        fig.set_figheight(2)
        fig.set_figwidth(30)

        mapping = {"0": 0, "+": 1, "-": -1}

        x = [i for i in range(len(binary))]
        y = [mapping[c] for c in binary]

        ax.step(x, y)
        ax.set_yticks([-1, 0, 1])
        ax.set_xlabel("Bit")
        ax.set_title("B8ZS Plot")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        canvas.get_tk_widget().grid(
            row=11, column=0, sticky="WE", padx=20, pady=(0, 10)
        )
