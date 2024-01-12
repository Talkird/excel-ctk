import customtkinter as ctk
from components.TabView import TabView
from theme import Theme

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.resizable(True, True)
        self.title("Automatizador Excel")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 1)

        self.tab_view = TabView(master=self).pack(fill="both", expand=True, padx=10, pady=10)

ctk.set_default_color_theme("green")
app = App()
app.mainloop()