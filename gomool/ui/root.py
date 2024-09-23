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
        self.geometry("600x400+200+200")
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
        self.frame1.pack(fill='both')#grid(row=0, column=0, sticky='nsew')
        font = get_font(FontName.CAMPTON_MEDIUM, size=15)
        self.keyframe = KeyFrame(self)
        self.keyframe.pack(fill='both')
        self.label = tk.Label(self, text="'F5' Hide Toggle / 'F7' Start Random Selection !!", font=font)
        self.label.pack(fill='both')
        font = get_font(FontName.CAMPTON_MEDIUM, size=15)
        self.select_song_label = tk.Label(self, text="No Selected", font=font, fg='green')
        self.select_song_label .pack(fill='both')
        # ICON
        self.iconphoto(False, tk.PhotoImage(file="./resource/gomool.png"))
        # Key Event
        self.after(100, self._key_event_handler)
        # State
        self.state = True
        
    def change_theme(self):
        if self.tk.call("ttk::style", "theme", "use") == "azure-dark":
            self.tk.call("set_theme", "light")
        else:
            self.tk.call("set_theme", "dark")
            
    def _get_random_select(self):
        keys = self.keyframe.get_keys()
        levels = self.levelframe.get_level()
        song = select_random(keys, levels)
        if song is None:
            text = "No Selected"
        else:
            text = f"{song[4]} - {song[2]} {song[5]} Lv.{song[6]}"
        self.select_song_label.configure(text=f"{text}")
        
    def _toggle_withdraw(self):
        self.state = not self.state
        if self.state:
            self.withdraw()
        else:
            self.deiconify()
            
    # Event
    def _key_event_handler(self):
        if is_key_trigger(Keys.F7):
            self._get_random_select()
        if is_key_trigger(Keys.F5):
            self._toggle_withdraw()
        self.after(100, self._key_event_handler)