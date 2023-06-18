from tkinter import *
from host import SocketServer


class HostInterface (Toplevel):
    server: SocketServer
    start_button: Button
    stop_button: Button
    status_field: Entry
    status: StringVar
    host_ip_field: Entry
    host_ip: StringVar
    status_field: Entry
    data: list[str]

    def __init__(self, root):
        super().__init__(root)
        root.eval(f'tk::PlaceWindow {str(self)} center')
        self.grab_set()
        self.grid_columnconfigure(0, weight=0)
        self.resizable(False, False)
        self.geometry("400x250")
        self.title("Host")
        self.server = SocketServer()
        self.host_ip = StringVar()
        self.status = StringVar()
        self.status.set("Stopped")

        self.host_ip_field = Entry(
            self, textvariable=self.host_ip, width=20, font=('calibre', 8, 'normal'))
        self.host_ip_field.grid(
            row=0, column=0, sticky="WE", padx=20, pady=(20, 10))
        self.host_ip_field.config(state="readonly")

        Button(self, anchor="center", width=20, text="Obter IP do Host", font=(
            'calibre', 8, 'normal'), bd="2.5p", command=self.get_host_ip).grid(row=1, column=0, padx=70)

        self.start_button = Button(self, anchor="center", width=20, text="Iniciar Servidor", font=(
            'calibre', 8, 'normal'), bd="2.5p", command=self.start_server)
        self.start_button.grid(row=2, column=0, padx=70)

        self.stop_button = Button(self, anchor="center", width=20, text="Parar Servidor", font=(
            'calibre', 8, 'normal'), bd="2.5p", command=self.stop_server)
        self.stop_button.grid(row=3, column=0, padx=70)
        self.stop_button.config(state="disabled")

        self.status_field = Entry(
            self, textvariable=self.status, width=20, font=('calibre', 8, 'normal'))
        self.status_field.grid(row=4, column=0, padx=70)
        self.status_field.config({"background": "Red"})

    def update(self):
        self.data = self.server.data

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
