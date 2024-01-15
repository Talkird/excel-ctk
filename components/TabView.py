import customtkinter as ctk
from widgets.Entry import Entry
from widgets.Button import Button
from widgets.Label import Label
from widgets.ComboBox import ComboBox
from theme import Theme
import openpyxl as xl

class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)

        #create tabs
        self.add("Contrato")
        self.add("Licencia")
        self.add("Implementación")
        self.add("Monitoreo")
        self.add("Resumen")

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
        self.entry_eps = Entry(master=self.tab("Licencia"), text="EPS")
        self.entry_eps.grid(sticky="w", row=0, column=1, padx=10, pady=5)

        self.label_margen = Label(master=self.tab("Licencia"), text="Margen [Porcentual]").grid(sticky="w", row=1, column=0, padx=10, pady=5)
        self.entry_margen = Entry(master=self.tab("Licencia"), text="Margen")
        self.entry_margen.grid(sticky="w", row=1, column=1, padx=10, pady=5)

        #Implementación
        self.label_experto = Label(master=self.tab("Implementación"), text="Experto implementación").grid(sticky="w", row=0, column=0, padx=10, pady=5)
        self.combo_experto_impl = ComboBox(master=self.tab("Implementación"), values=["Exp 1", "Exp 2", "Exp 3", "Exp 4"])
        self.combo_experto_impl.grid(sticky="w", row=0, column=1, padx=10, pady=5)
        
        self.label_horas_impl = Label(master=self.tab("Implementación"), text="Horas de trabajo").grid(sticky="w", row=1, column=0, padx=10, pady=5)
        self.horas_impl = Entry(master=self.tab("Implementación"), text="Horas")
        self.horas_impl.grid(sticky="w", row=1, column=1, padx=10, pady=5)

        #Monitoreo
        self.label_monitoreo = Label(master=self.tab("Monitoreo"), text="Turno")
        self.label_monitoreo.grid(row=0, column=0, sticky="w", padx=10, pady=15)

        self.turno_monitoreo = ComboBox(master=self.tab("Monitoreo"), values=["Diurno", "Nocturno", "24x7"])
        self.turno_monitoreo.grid(row=0, column=1, sticky="w", padx=10, pady=15)

        #SLOT 1
        self.experto1 = ComboBox(master=self.tab("Monitoreo"), values=["Exp 1", "Exp 2", "Exp 3", "Exp 4"])
        self.experto1.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.horas_experto1 = Entry(master=self.tab("Monitoreo"), text="Horas")
        self.horas_experto1.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        #SLOT 2
        self.experto2 = ComboBox(master=self.tab("Monitoreo"), values=["Exp 1", "Exp 2", "Exp 3", "Exp 4"])
        self.experto2.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.horas_experto2 = Entry(master=self.tab("Monitoreo"), text="Horas")
        self.horas_experto2.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        #SLOT 3
        self.experto3 = ComboBox(master=self.tab("Monitoreo"), values=["Exp 1", "Exp 2", "Exp 3", "Exp 4"])
        self.experto3.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        self.horas_experto3 = Entry(master=self.tab("Monitoreo"), text="Horas")
        self.horas_experto3.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        #SLOT 4
        self.experto4 = ComboBox(master=self.tab("Monitoreo"), values=["Exp 1", "Exp 2", "Exp 3", "Exp 4"])
        self.experto4.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.horas_experto4 = Entry(master=self.tab("Monitoreo"), text="Horas")
        self.horas_experto4.grid(row=4, column=1, sticky="w", padx=10, pady=5)

        #Finalizar
        self.button_finalizar = Button(master=self.tab("Resumen"), text="Finalizar", command=self.generar_costo).pack(anchor="w", padx=10, pady=5)

        self._segmented_button.configure(font=Theme.font, selected_color=Theme.accent, selected_hover_color=Theme.accent_hover)


    def generar_costo(self):
        wb = xl.load_workbook("configurador.xlsx", data_only=False)
        sheet = wb["Cotizador EPS"]

        # Assuming self.entry_eps is a numerical value
        sheet["C7"] = float(self.entry_eps.get())

        # Assuming self.entry_margen is a percentage string, e.g., "15%"
        percentage_value = float(self.entry_margen.get().strip('%')) / 100
        sheet["C8"] = percentage_value

        sheet["C13"] = self.combo_experto_impl.get()
        sheet["D13"] = float(self.horas_impl.get())

        # Save the changes to the Excel file
        wb.save("configurador.xlsx")
