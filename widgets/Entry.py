import customtkinter as ctk
from theme import Theme

class Entry(ctk.CTkEntry):
    def __init__(self, master, text: str):
        super().__init__(master, placeholder_text=text, font=Theme.font)
