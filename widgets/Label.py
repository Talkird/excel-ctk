import customtkinter as ctk
from theme import Theme

class Label(ctk.CTkLabel):
    def __init__(self, master, text: str):
        super().__init__(master, text=text, font=Theme.font)
