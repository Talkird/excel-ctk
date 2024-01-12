import customtkinter as ctk
from theme import Theme
from widgets.Entry import Entry
from widgets.Button import Button

class Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)

        self.text_horas = Entry(master=self, text="1").pack(anchor="w", padx=10, pady=5)
        self.text_horas1 = Entry(master=self, text="2").pack(anchor="w", padx=10, pady=5)

        self.button = Button(master=self, text="Crear Excel", command=lambda: print("asd")).pack(anchor="se", padx=10, pady=5)



        self.pack(fill="both", expand=True, padx=15, pady=15)