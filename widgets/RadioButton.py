import customtkinter as ctk
from theme import Theme

class RadioButton(ctk.CTkRadioButton):
    def __init__(self, master, text: str, value, variable, command):
        super().__init__(master, text=text, font=Theme.font, variable=variable, value=value, fg_color=Theme.accent, hover_color=Theme.accent_hover, command=command)
