import tkinter as tk
import tkinter.font as font
import enum

class FontName(enum.Enum):
    CAMPTON_BOOK = "Campton Book"
    CAMPTON_BOLD = "Campton Bold"

def get_font(name: FontName, size=12):
    return font.Font(family=name.value, size=size)