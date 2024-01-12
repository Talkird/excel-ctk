import customtkinter as ctk
from theme import Theme
from widgets.Label import Label
from widgets.Button import ButtonNoCorners

def close_menu() -> None: exit(0)
 
class TitleBar(ctk.CTkFrame):
    def __init__(self, master, title: str):
        super().__init__(master, corner_radius=0)

        self.title_label = Label(master=self, text=title)
        self.title_label.pack(anchor="nw", side="left", padx=(120, 0))

        self.close_button = ButtonNoCorners(master=self, text="✕", width=50, command=close_menu)
        self.close_button.pack(anchor="ne", side="right")
        
        self.pack(fill="x", anchor="n")

        def get_pos(event):
            xwin = master.winfo_x()
            ywin = master.winfo_y()
            startx = event.x_root
            starty = event.y_root

            ywin = ywin - starty
            xwin = xwin - startx

            def move_window(event):
                master.geometry("600x300" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
                startx = event.x_root
                starty = event.y_root

            self.bind('<B1-Motion>', move_window)
            self.title_label.bind('<B1-Motion>', move_window)

        self.bind('<Button-1>', get_pos)
        self.title_label.bind('<Button-1>', get_pos)
