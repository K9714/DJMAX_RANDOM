import tkinter as tk
from ..event import *

class ImageToggle(tk.Frame):
    def __init__(self, root, font, on_image, off_image, *args, text="", **kwargs):
        super().__init__(root, *args, **kwargs)
        self.text = text
        self.font = font
        self.state = True
        self.images = {}
        self.images[True] = on_image
        self.images[False] = off_image
        
        self.button = tk.Label(self, text=text, image=self.images[self.state], border=0, font=font, compound='center', highlightcolor='black', highlightbackground='black', highlightthickness=1, fg='#f9ecf1')
        self.button.pack()
        
        self.button.bind(MouseEvent.LEFT_RELEASE, self.click_event)

    def click_event(self, event):
        self.state = not self.state
        self.button.configure(image=self.images[self.state])