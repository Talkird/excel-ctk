import customtkinter as ctk
from components.TabView import TabView
from components.TitleBar import TitleBar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.resizable(False, False)
        self.title("Automatizador Excel")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 1)
        self.overrideredirect(True)

        self.title_bar = TitleBar(master=self, title="Automatizador Excel").pack(fill="x", expand=True)
        self.tab_view = TabView(master=self).pack(fill="both", expand=True, padx=15, pady=15)

ctk.set_default_color_theme("green")
app = App()
app.mainloop()