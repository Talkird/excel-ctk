import customtkinter as ctk
from components.Frame import Frame
from components.TitleBar import TitleBar
from theme import Theme

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x280")
        self.resizable(False, False)
        self.title("Automatizacor Excel")
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.95)

        #widgets
        self.title_bar = TitleBar(master=self, title="Automatizador Excel")
        self.frame = Frame(master=self)

ctk.set_default_color_theme("green")
app = App()
app.mainloop()