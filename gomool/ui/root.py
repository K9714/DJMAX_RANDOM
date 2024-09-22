import tkinter as tk
import tkinter.font as font

class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Theme
        self.tk.call("source", "./resource/azure.tcl")
        self.tk.call("set_theme", "dark")
        
    def change_theme(self):
        if self.tk.call("ttk::style", "theme", "use") == "azure-dark":
            self.tk.call("set_theme", "light")
        else:
            self.tk.call("set_theme", "dark")