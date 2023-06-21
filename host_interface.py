from tkinter import *
from host import SocketServer


class HostInterface(Toplevel):
    server: SocketServer
    start_button: Button
    stop_button: Button
    status_field: Entry
    status: StringVar
    host_ip_field: Entry
    host_ip: StringVar
    status_field: Entry

    def __init__(self, root):
        super().__init__(root)
        root.eval(f"tk::PlaceWindow {str(self)} center")
        self.grab_set()
        self.title("Host")

        self.server = SocketServer(callback=self.update)

        self.host_ip = StringVar()
        self.status = StringVar()
        self.data = StringVar()
        self.message = StringVar()
        self.encrypted_message = StringVar()
        self.binary_message = StringVar()

        self.status.set("Stopped")
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.geometry("1024x600")


        #ip input field -------------

        self.label_text_input_connect = Label(
            self, text="IP do Host", font=("arial", 12)
        )
        self.label_text_input_connect.grid(column=0, row=0, sticky="W", padx=(20, 20))

        self.host_ip_field = Entry(
            self, textvariable=self.host_ip, width=20, font=("calibre", 8, "normal")
        )
        self.host_ip_field.grid(row=1, column=0, sticky="WE", padx=(20, 20), pady=(0, 10))
        self.host_ip_field.config(state="readonly")

        # control buttons -------------

        Button(
            self,
            anchor="center",
            width=20,
            text="Obter IP do Host",
            font=("calibre", 8, "normal"),
            bd="2.5p",
            command=self.get_host_ip,
        ).grid(row=2, column=0, padx=20)

        self.start_button = Button(
            self,
            anchor="center",
            width=20,
            text="Iniciar Servidor",
            font=("calibre", 8, "normal"),
            bd="2.5p",
            command=self.start_server,
        )
        self.start_button.grid(row=1, column=1, padx=20)

        self.stop_button = Button(
            self,
            anchor="center",
            width=20,
            text="Parar Servidor",
            font=("calibre", 8, "normal"),
            bd="2.5p",
            command=self.stop_server,
        )
        self.stop_button.grid(row=1, column=2, padx=20)
        self.stop_button.config(state="disabled")

        #server status display ----------
        self.status_field = Entry(
            self, textvariable=self.status, width=20, font=("calibre", 8, "normal")
        )
        self.status_field.grid(row=1, column=3, padx=20)
        self.status_field.config({"background": "Red"})

        # message text display ------------
        self.label_message = Label(self, text="Mensagem", font=("arial", 12))
        self.label_message.grid(column=0, row=4, sticky="W", padx=20)

        self.received_message_text = Entry(
            self, textvariable=self.message, font=("arial", 8, "normal")
        )
        self.received_message_text.grid(
            row=5, column=0, sticky="WE", padx=20, pady=(0, 10)
        )
        self.received_message_text.config(state="readonly")


        # encrypted message display ------------
        self.label_message = Label(self, text="Mensagem Encriptada", font=("arial", 12))
        self.label_message.grid(column=0, row=6, sticky="W", padx=20)

        self.received_message_text = Entry(
            self, textvariable=self.encrypted_message, font=("arial", 8, "normal")
        )
        self.received_message_text.grid(
            row=7, column=0, sticky="WE", padx=20, pady=(0, 10)
        )
        self.received_message_text.config(state="readonly")

        # binary message display ------------
        self.label_message = Label(self, text="Mensagem Binária", font=("arial", 12))
        self.label_message.grid(column=0, row=8, sticky="W", padx=20)

        self.received_message_text = Entry(
            self, textvariable=self.encrypted_message, font=("arial", 8, "normal")
        )
        self.received_message_text.grid(
            row=9, column=0, sticky="WE", padx=20, pady=(0, 10)
        )
        self.received_message_text.config(state="readonly")

        # b8zs message display ------------
        self.label_message = Label(self, text="B8zs", font=("arial", 12))
        self.label_message.grid(column=0, row=10, sticky="W", padx=20)

        self.received_message_text = Entry(
            self, textvariable=self.encrypted_message, font=("arial", 8, "normal")
        )
        self.received_message_text.grid(
            row=11, column=0, sticky="WE", padx=20, pady=(0, 10)
        )
        self.received_message_text.config(state="readonly")


        #self.received_messages = Text(self, height=5, width=160, font=("arial", 10))
        #self.received_messages.grid(column=0, row=5, sticky="W", padx=20)

    def update(self):
        self.received_messages.insert(END, self.server.data)

    def get_host_ip(self):
        self.host_ip.set(self.server.get_host())

    def start_server(self):
        self.status.set("Running")
        self.status_field.config({"background": "Green"})
        self.stop_button.config(state="normal")
        self.start_button.config(state="disabled")
        self.server.start_server()

    def stop_server(self):
        self.status.set("Stopped")
        self.status_field.config({"background": "Red"})
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.server.close_server()
