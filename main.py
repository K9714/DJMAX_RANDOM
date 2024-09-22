from gomool.ui.root import Root
from gomool.ui.font import get_font, FontName
from gomool.ui.frame import *
import tkinter as tk

root = Root()
root.overrideredirect(True)
root.geometry("800x600+200+200")

font = get_font(FontName.CAMPTON_BOOK)
titlebar = TitleBar(root, "DJMAX Music Random Selector - GOMOOL", font=font)
font = get_font(FontName.CAMPTON_BOOK, size=15)
levelFrame = LevelFrame(root, font)
levelFrame.pack()
# label = tk.Label(root, text="DJMAX RANDOM SELECTOR - GOMOOL", font=font)
# label.pack()

# btn = tk.Button(legend, text="asdasd")
# btn.pack()

root.iconphoto(False, tk.PhotoImage(file="./resource/gomool.png"))


root.mainloop()