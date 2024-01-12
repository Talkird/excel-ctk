import customtkinter as ctk
from theme import Theme

class ComboBox(ctk.CTkComboBox):
    def __init__(self, master, values):
        super().__init__(master, values=values, font=Theme.font)
