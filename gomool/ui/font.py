import tkinter as tk
import tkinter.font as font
import enum

class FontName(enum.Enum):
    CAMPTON_BOLD = "Campton Book"
    CAMPTON_EXTRA_BOLD = "Campton ExtraBold"
    CAMPTON_MEDIUM = "Campton Medium"
    CAMPTON_LIGHT = "Campton Light"
    CAMPTON_SEMI_BOLD = "Campton SemiBold"

def get_font(name: FontName, size=12):
    return font.Font(family=name.value, size=size)