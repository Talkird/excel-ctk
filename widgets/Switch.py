import customtkinter as ctk
from theme import Theme

class Switch(ctk.CTkSwitch):
    def __init__(self, master, text: str):
        super().__init__(master, text=text, font=("Tahoma", 16), progress_color=Theme.accent)
