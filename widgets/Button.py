import customtkinter as ctk
from theme import Theme

class Button(ctk.CTkButton):
    def __init__(self, master, text: str, command, width=None, height=None):
        super().__init__(master, text=text, font=Theme.font, fg_color=Theme.accent, hover_color=Theme.accent_hover, command=command)

        if width is not None:
            self.configure(width=width)

        if height is not None:
            self.configure(height=height)


class ButtonNoCorners(ctk.CTkButton):
    def __init__(self, master, text: str, command, width=None, height=None):
        super().__init__(master, text=text, font=Theme.font, fg_color=Theme.accent, hover_color=Theme.accent_hover, command=command, corner_radius=0)
    
        if width is not None:
            self.configure(width=width)

        if height is not None:
            self.configure(height=height)