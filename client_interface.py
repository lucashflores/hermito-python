from tkinter import *


class ClientInterface(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.text_input = StringVar()
        # self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.geometry("800x600")
        self.title("Client")

        self.label = Label(self, text="Cliente", font=("Arial", 30))
        self.button = Button()

        # Label(self, text="asdasd", font=('calibre', 8, 'normal')).grid(
        #     row=0, column=0, sticky="W", padx=20, pady=(10, 5))
        # Entry(self, textvariable=self.text_input, font=('calibre', 8, 'normal')).grid(
        #     row=1, column=0, sticky="WE", padx=20, pady=(0, 10))
        # Button(self, anchor="center", width=10, text="OK", font=('calibre', 8, 'normal'),
        #        bd="2.5p", command=self.update_with_input).grid(row=2, sticky="W", column=0, padx=70)
        # Button(self, anchor="center", width=10, text="Cancel", font=('calibre', 8, 'normal'), bd='1.5p',
        #        command=lambda ans="": self.update_answer(ans)).grid(row=2, sticky="E", column=0, padx=70)
