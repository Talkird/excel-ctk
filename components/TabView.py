import customtkinter as ctk
from widgets.Entry import Entry
from widgets.Button import Button
from widgets.Label import Label
from widgets.ComboBox import ComboBox
from widgets.RadioButton import RadioButton
from theme import Theme

class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)

        #create tabs
        self.add("Contrato")
        self.add("Licencia")
        self.add("Implementación")
        self.add("Monitoreo")
        self.add("Finalizar")

        #Contrato
        self.label_cliente = Label(master=self.tab("Contrato"), text="Cliente").grid(sticky='w', row=0, column=0, padx=10, pady=5)
        self.entry_cliente = Entry(master=self.tab("Contrato"), text="Cliente").grid(row=0, column=1, padx=10, pady=5)

        self.label_pais= Label(master=self.tab("Contrato"), text="País de cliente").grid(sticky='w', row=1, column=0, padx=10, pady=5)
        self.combo_pais_cliente = ComboBox(master=self.tab("Contrato"), values=["Argentina", "Chile", "Brazil", "Spain", "Mexico", "Ecuador", "Colombia", "Otro"]).grid(row=1, column=1, padx=10, pady=5)

        self.label_fact = Label(master=self.tab("Contrato"), text="País de facturación").grid(sticky='w', row=2, column=0, padx=10, pady=5)
        self.combo_pais_fact = ComboBox(master=self.tab("Contrato"), values=["Argentina", "Chile", "Brazil", "Spain"]).grid(row=2, column=1, padx=10, pady=5)

        self.label_moneda = Label(master=self.tab("Contrato"), text="Moneda de cotización").grid(sticky='w', row=3, column=0, padx=10, pady=5)
        self.combo_moneda_fact = ComboBox(master=self.tab("Contrato"), values=["USD", "UF", "ARS", "MEP", "CLP", "EUR", "REAL"]).grid(row=3, column=1, padx=10, pady=5)

        #Licencia
        self.label_eps = Label(master=self.tab("Licencia"), text="EPS").grid(sticky="w", row=0, column=0, padx=10, pady=5)
        self.entry_horas = Entry(master=self.tab("Licencia"), text="EPS").grid(sticky="w", row=0, column=1, padx=10, pady=5)

        self.label_margen = Label(master=self.tab("Licencia"), text="Margen [Porcentual]").grid(sticky="w", row=1, column=0, padx=10, pady=5)
        self.entry_margen = Entry(master=self.tab("Licencia"), text="Margen").grid(sticky="w", row=1, column=1, padx=10, pady=5)

        #Implementación
        self.label_experto = Label(master=self.tab("Implementación"), text="Experto implementación").grid(sticky="w", row=0, column=0, padx=10, pady=5)
        self.combo_experto_impl = ComboBox(master=self.tab("Implementación"), values=["Experto1", "Experto2", "Experto3", "Experto4"]).grid(sticky="w", row=0, column=1, padx=10, pady=5)
        
        self.label_horas_impl = Label(master=self.tab("Implementación"), text="Horas de trabajo").grid(sticky="w", row=1, column=0, padx=10, pady=5)
        self.horas_impl = Entry(master=self.tab("Implementación"), text="Horas").grid(sticky="w", row=1, column=1, padx=10, pady=5)

        #Monitoreo
        radio_var = ctk.StringVar()
        self.radio_diurno = RadioButton(master=self.tab("Monitoreo"), text="Diurno", value="diurno", variable=radio_var, command=None).grid(sticky="w", row=0, column=0, padx=10, pady=5)
        self.radio_nocturno = RadioButton(master=self.tab("Monitoreo"), text="Nocturno", value="nocturno", variable=radio_var, command=None).grid(sticky="w", row=1, column=0, padx=10, pady=5)
        self.radio_completo = RadioButton(master=self.tab("Monitoreo"), text="24x7", value="completo", variable=radio_var, command=None).grid(sticky="w", row=2, column=0, padx=10, pady=5)

        #Finalizar
        self.button_finalizar = Button(master=self.tab("Finalizar"), text="Finalizar", command=lambda: print("test")).pack(anchor="w", padx=10, pady=5)

        self._segmented_button.configure(font=Theme.font, selected_color=Theme.accent, selected_hover_color=Theme.accent_hover)
