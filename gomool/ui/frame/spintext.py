import tkinter as tk
from ..event import *

class SpinText(tk.Frame):
    def __init__(self, root, font, min_value, max_value, *args, value=0, text="", **kwargs):
        super().__init__(root, *args, **kwargs)
        self.text = text
        self.font = font
        self.event_handler = []
        self.min_value = min_value
        self.max_value = max_value
        self.value = max(min(value, self.max_value), self.min_value)
        self.strvar = tk.StringVar()
        self.strvar.set(f"{self.value}")
        
        self.text_frame = tk.Frame(self)
        # label.pack(fill='both')
        self.value_frame = tk.Frame(self)
        self.decrease_btn = tk.Button(self.value_frame, text="◀", bg="#675547", font=self.font, border=0)
        self.increase_btn = tk.Button(self.value_frame, text="▶", bg="#675547", font=self.font, border=0)
        widgets: list[tk.Widget] = [
            tk.Label(self.value_frame, text=text, bg="#3c3631", font=self.font),
            self.decrease_btn,
            tk.Label(self.value_frame, textvariable=self.strvar, bg="#675547", font=self.font),
            self.increase_btn
        ]
        self.value_frame.columnconfigure(index=0, weight=2, uniform=1)
        self.value_frame.columnconfigure(index=1, weight=1, uniform=1)
        self.value_frame.columnconfigure(index=2, weight=1, uniform=1)
        self.value_frame.columnconfigure(index=3, weight=1, uniform=1)
        widgets[1].bind(MouseEvent.LEFT_RELEASE, self.decrease_click, "+")
        widgets[3].bind(MouseEvent.LEFT_RELEASE, self.increase_click, "+")
        for i in range(4):
            # self.value_frame.rowconfigure(0, weight=1, uniform=1)
            widgets[i].grid(row=0, column=i, sticky='nsew')
        # Config
        self.rowconfigure(0, weight=1, uniform=1)
        self.columnconfigure(0, weight=1, uniform=1)
        # self.columnconfigure(1, weight=1, uniform=1)
        # self.text_frame.grid(row=0, column=0, sticky='nsew')
        self.value_frame.grid(row=0, column=0, sticky='nsew')

    def add_event(self, fn=None):
        self.event_handler.append(fn)
        
    def _call_events(self, event):
        for fn in self.event_handler:
            fn(event)
            
    def decrease_click(self, event):
        self.value = max(self.value - 1, self.min_value)
        self.strvar.set(f"{self.value}")
        self._call_events(event)

    def increase_click(self, event):
        self.value = min(self.value + 1, self.max_value)
        self.strvar.set(f"{self.value}")
        self._call_events(event)