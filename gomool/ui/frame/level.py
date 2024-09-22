import tkinter as tk
from .spintext import SpinText
from ..event import *

class LevelFrame(tk.Frame):
    def __init__(self, root, font, **kwargs):
        super().__init__(root, **kwargs)
        self.font = font
        self.lv_png = {
            "NM": [
                tk.PhotoImage(file="./resource/djmax/level/nm_black.png"),
                tk.PhotoImage(file="./resource/djmax/level/nm_star.png"),
                tk.PhotoImage(file="./resource/djmax/level/hd_star.png"),
                tk.PhotoImage(file="./resource/djmax/level/mx_star.png"),
            ],
            "SC": [ 
                tk.PhotoImage(file="./resource/djmax/level/sc_nm_black.png"),
                tk.PhotoImage(file="./resource/djmax/level/sc_nm_star.png"),
                tk.PhotoImage(file="./resource/djmax/level/sc_hd_star.png"),
                tk.PhotoImage(file="./resource/djmax/level/sc_mx_star.png"),
            ]
        }
        self.max_level = 15
        self._set_frame()
        self._set_grid()
        self.bind(MouseEvent.LEFT_TRIGGER, self.update_level)

    def get_level(self):
        nm_min = self.normal_min.value
        nm_max = self.normal_max.value
        sc_min = self.sc_min.value
        sc_max = self.sc_max.value
        return nm_min, nm_max, sc_min, sc_max
        
    def update_level(self, event):
        normal_min = self.normal_min.value
        normal_max = self.normal_max.value
        for i, label in enumerate(self.normal_level_labels):
            if normal_min <= i + 1 <= normal_max:
                idx = i // 5 + 1
                label.configure(image=self.lv_png["NM"][idx])
            else:
                label.configure(image=self.lv_png["NM"][0])
        sc_min = self.sc_min.value
        sc_max = self.sc_max.value
        for i, label in enumerate(self.sc_level_labels):
            if sc_min <= i + 1 <= sc_max:
                idx = i // 5 + 1
                label.configure(image=self.lv_png["SC"][idx])
            else:
                label.configure(image=self.lv_png["SC"][0])
        
    def _set_frame(self):
        # Normal Level Frame
        self.normal_level_frame = tk.Frame(self)
        self.normal_level_labels: list[tk.Label] = []
        for i in range(self.max_level):
            self.normal_level_frame.columnconfigure(index=i, weight=1)
            lv = i
            idx = lv // 5 + 1
            label = tk.Label(self.normal_level_frame, image=self.lv_png["NM"][idx])
            label.grid(row=0, column=i, padx=0, sticky='nsew')
            self.normal_level_labels.append(label)
        # SC Level Frame
        self.sc_level_frame = tk.Frame(self)
        self.sc_level_labels: list[tk.Label] = []
        for i in range(self.max_level):
            self.sc_level_frame .columnconfigure(index=i, weight=1)
            lv = i
            idx = lv // 5 + 1
            label = tk.Label(self.sc_level_frame , image=self.lv_png["SC"][idx])
            label.grid(row=0, column=i, padx=0, sticky='nsew')
            self.sc_level_labels.append(label)
        # Noraml Level Min-Max Frame
        self.normal_mm_frame = tk.Frame(self)
        self.normal_min = SpinText(self.normal_mm_frame, self.font, 1, self.max_level, value=1, text="MIN")
        self.normal_max = SpinText(self.normal_mm_frame, self.font, 1, self.max_level, value=self.max_level, text="MAX")
        self.normal_min.add_event(self.update_level)
        self.normal_max.add_event(self.update_level)
        widgets: tk.Widget = [
            self.normal_min,
            self.normal_max
        ]
        for i in range(2):
            self.normal_mm_frame.columnconfigure(index=i, weight=1, uniform=1)
            widgets[i].grid(row=0, column=i, padx=2, pady=2, sticky='nsew')
        # SC Level Min-Max Frame
        self.sc_mm_frame = tk.Frame(self)
        self.sc_min = SpinText(self.sc_mm_frame, self.font, 1, self.max_level, value=1, text="MIN")
        self.sc_max = SpinText(self.sc_mm_frame, self.font, 1, self.max_level, value=self.max_level, text="MAX")
        self.sc_min.add_event(self.update_level)
        self.sc_max.add_event(self.update_level)
        widgets: tk.Widget = [
            self.sc_min,
            self.sc_max
        ]
        for i in range(2):
            self.sc_mm_frame.columnconfigure(index=i, weight=1, uniform=1)
            widgets[i].grid(row=0, column=i, padx=2, pady=2, sticky='nsew')
        
    def _set_grid(self):
        self.rowconfigure(index=0, weight=1, uniform=1)
        self.rowconfigure(index=1, weight=1, uniform=1)
        self.rowconfigure(index=2, weight=1, uniform=1)
        self.rowconfigure(index=3, weight=1, uniform=1)
        self.normal_level_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.normal_mm_frame.grid(row=1, column=0, padx=5, pady=2, sticky='nsew')
        self.sc_level_frame.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.sc_mm_frame.grid(row=3, column=0, padx=5, pady=2, sticky='nsew')