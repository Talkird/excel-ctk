import customtkinter as ctk
from components.Frame import Frame
from components.TitleBar import TitleBar
from components.TabView import TabView
from theme import Theme

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.resizable(False, False)
        self.title("Automatizacor Excel")
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.95)

        self.title_bar = TitleBar(master=self, title="Automatizador Excel")
        self.tab_view = TabView(master=self).pack(fill="both", expand=True, padx=15, pady=15)
        #self.frame = Frame(master=self)

ctk.set_default_color_theme("green")
app = App()
app.mainloop()