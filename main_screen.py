from tkinter import *
from host_interface import HostInterface


class MainScreen(Tk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.geometry("250x150")
        self.title("Main")
        Button(self, anchor="center", width=20, text="Client", font=('calibre', 8, 'normal'),
               bd="2.5p", command=self.start_as_client).grid(row=0, column=0, padx=25, pady=25)
        Button(self, anchor="center", width=20, text="Host", font=('calibre', 8, 'normal'),
               bd="2.5p", command=self.start_as_host).grid(row=1, column=0, padx=25)

    def start_as_client(self):
        return False

    def start_as_host(self):
        host_screen = HostInterface(self)
