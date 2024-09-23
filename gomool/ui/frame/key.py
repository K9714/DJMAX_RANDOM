
import tkinter as tk
from .imagetoggle import ImageToggle
from ..font import *
from ..event import *

class KeyFrame(tk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.key_png = {
            "4B": tk.PhotoImage(file="./resource/djmax/4B.png"),
            "4Boff": tk.PhotoImage(file="./resource/djmax/4B_disable.png"),
            "5B": tk.PhotoImage(file="./resource/djmax/5B.png"),
            "5Boff": tk.PhotoImage(file="./resource/djmax/5B_disable.png"),
            "6B": tk.PhotoImage(file="./resource/djmax/6B.png"),
            "6Boff": tk.PhotoImage(file="./resource/djmax/6B_disable.png"),
            "8B": tk.PhotoImage(file="./resource/djmax/8B.png"),
            "8Boff": tk.PhotoImage(file="./resource/djmax/8B_disable.png"),
        }
        self._set_frame()
        self._set_grid()

    def get_keys(self):
        keys = []
        if self._4b.state:
            keys.append(4)
        if self._5b.state:
            keys.append(5)
        if self._6b.state:
            keys.append(6)
        if self._8b.state:
            keys.append(8)
        return keys
        
    def _set_frame(self):
        font = get_font(FontName.CAMPTON_EXTRA_BOLD, size=25)
        self._4b = ImageToggle(self, font, self.key_png['4B'], self.key_png['4Boff'], text="4B")
        self._5b = ImageToggle(self, font, self.key_png['5B'], self.key_png['5Boff'], text="5B")
        self._6b = ImageToggle(self, font, self.key_png['6B'], self.key_png['6Boff'], text="6B")
        self._8b = ImageToggle(self, font, self.key_png['8B'], self.key_png['8Boff'], text="8B")
        
    def _set_grid(self):
        self.rowconfigure(index=0, weight=1, uniform=1)
        self.columnconfigure(index=0, weight=1, uniform=1)
        self.columnconfigure(index=1, weight=1, uniform=1)
        self.columnconfigure(index=2, weight=1, uniform=1)
        self.columnconfigure(index=3, weight=1, uniform=1)
        self._4b.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self._5b.grid(row=0, column=1, padx=5, pady=2, sticky='nsew')
        self._6b.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        self._8b.grid(row=0, column=3, padx=5, pady=2, sticky='nsew')