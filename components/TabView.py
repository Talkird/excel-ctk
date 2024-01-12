import customtkinter as ctk
from widgets.Entry import Entry

class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)

        #create tabs
        self.add("Contrato")
        self.add("Licencia")
        self.add("Impl")
        self.add("Finalizar")

        #Contrato
        self.cliente = Entry(master=self.tab("Contrato"), text="Cliente").pack(anchor="w", padx=10, pady=5)
        self.pais_cliente = ctk.CTkComboBox(master=self.tab("Contrato"), values=["Argentina", "Chile", "Brazil", "Spain", "Mexico", "Ecuador", "Colombia", "Otro"]).pack(anchor="w", padx=10, pady=5)
        self.pais_fact = ctk.CTkComboBox(master=self.tab("Contrato"), values=["Argentina", "Chile", "Brazil", "Spain"]).pack(anchor="w", padx=10, pady=5)
        self.moneda_fact = ctk.CTkComboBox(master=self.tab("Contrato"), values=["USD", "UF", "ARS", "MEP", "CLP", "EUR", "REAL"]).pack(anchor="w", padx=10, pady=5) 

        #Licencia
        self.text_horas = Entry(master=self.tab("Licencia"), text="EPS").pack(anchor="w", padx=10, pady=5)
        self.text_horas1 = Entry(master=self.tab("Licencia"), text="Margen").pack(anchor="w", padx=10, pady=5)

        self._segmented_button.configure(font=("Roboto", 16))


    def calcular_licencia(EPS: int) -> float:
        pass