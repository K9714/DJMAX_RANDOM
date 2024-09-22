import tkinter as tk
from .font import get_font, FontName
from .event import *
from .frame import *
from ..util import *

class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Theme
        self.tk.call("source", "./resource/azure.tcl")
        self.tk.call("set_theme", "dark")
        # SIZE
        self.overrideredirect(True)
        self.geometry("800x600+200+200")
        # Frame
        font = get_font(FontName.CAMPTON_BOLD)
        self.titlebar = TitleBar(self, "DJMAX Music Random Selector - GOMOOL", font=font, bg='#2b2b2b')
        font = get_font(FontName.CAMPTON_BOLD, size=15)
        self.frame1 = tk.Frame()
        self.frame1.columnconfigure(0, weight=1, uniform=1)
        self.frame1.columnconfigure(1, weight=4, uniform=1)
        self.levelframe = LevelFrame(self.frame1, font)
        self.levelframe.grid(row=0, column=1, sticky='nsew')
        font = get_font(FontName.CAMPTON_EXTRA_BOLD, size=20)
        self.levellabel = tk.Label(self.frame1, text="LEVEL", bg="#291b14", font=font)
        self.levellabel.grid(row=0, column=0, sticky='nsew')
        self.frame1.pack()#grid(row=0, column=0, sticky='nsew')
        font = get_font(FontName.CAMPTON_SEMI_BOLD, size=15)
        self.label = tk.Label(self, text="Press 'F7' key !!", font=font)
        self.label.pack()
        # ICON
        self.iconphoto(False, tk.PhotoImage(file="./resource/gomool.png"))
        # Key Event
        self.after(100, self._key_event_handler)
        
    def change_theme(self):
        if self.tk.call("ttk::style", "theme", "use") == "azure-dark":
            self.tk.call("set_theme", "light")
        else:
            self.tk.call("set_theme", "dark")
            
    def _get_random_select(self):
        keys = [4]#, 5, 6, 8]
        levels = self.levelframe.get_level()
        select_random(keys, levels)
            
    # Event
    def _key_event_handler(self):
        if is_key_trigger(Keys.F7):
            self._get_random_select()
        self.after(100, self._key_event_handler)