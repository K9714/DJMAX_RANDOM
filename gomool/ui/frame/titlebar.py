import tkinter as tk
import tkinter.font as font
from ctypes import windll
from ..event import *

class TitleBar(tk.Frame):
    def __init__(self, parent, title, font, **kwargs):
        self.parent = parent
        super().__init__(self.parent, **kwargs)
        self.title = title
        self.parent.title(self.title)
        self.font = font
        self.maximized = False
        self.hasstyle = False
        self.parent.windowSize = [self.parent.winfo_width(), 
                                  self.parent.winfo_height()]
        self.back_ground = "#2c2c2c"

        self.parent.withdraw()
        self.parent.update()
        dims = [int(x) for x in self.parent.geometry().split('+')[0].split('x')]
        dimension = (dims[0], dims[1])

        x = (self.parent.winfo_screenwidth()/2)-(dimension[0]/2)
        y = (self.parent.winfo_screenheight()/2)-250
        self.parent.geometry(f'{dimension[0]}x{dimension[1]}+{int(x)}+{int(y)}')
        self.parent.minsize(dimension[0], dimension[1])
        self.previousPosition = [int(x), int(y)]

        self.__ParentFrame__()
        self.__events__()
        self.loop_control()

    '''GUI Private Methods'''
    def __events__(self):
        self.minimize_btn.bind(MouseEvent.ENTER, lambda x: self.minimize_btn.configure(bg='#777777'))
        self.minimize_btn.bind(MouseEvent.LEAVE, lambda x: self.minimize_btn.configure(bg=self.back_ground))
        self.close_button.bind(MouseEvent.ENTER, lambda x: self.close_button.configure(bg='red'))
        self.close_button.bind(MouseEvent.LEAVE, lambda x: self.close_button.configure(bg=self.back_ground))

    def __ParentFrame__(self):
        self.parent.overrideredirect(True)

        #title bar
        self.title_bar = tk.Frame(self.parent)

        #window title
        self.title_name = tk.Label(self.title_bar, text=self.title, 
                             font=self.font)

        #minimize btn
        self.minimize_btn = tk.Button(self.title_bar, text='_', bg=self.back_ground, padx=5, pady=2, 
                                 bd=0, font=self.font, fg='white', width=2,
                                 activebackground="red",
                                 activeforeground="white", 
                                 highlightthickness=0, 
                                 command=self.minimize)

        #maximize btn
        # self.maximize_btn = tk.Button(self.title_bar, text='🗖', bg=self.back_ground, padx=5, pady=2, 
        #                          bd=0, font="bold", fg='white', width=2,
        #                          activebackground="red",
        #                          activeforeground="white", 
        #                          highlightthickness=0, 
        #                          command=self.maximizeToggle)

        #close btn
        self.close_button = tk.Button(self.title_bar, text='X', bg=self.back_ground, padx=5, pady=2, 
                                 bd=0, font=self.font, fg='white', width=2,
                                 activebackground="red",
                                 activeforeground="white", 
                                 highlightthickness=0, 
                                 command=self.quit)

        # pack the widgets
        self.title_bar.pack(fill='x', side=tk.TOP)
        self.title_name.pack(side='left', padx=5)
        self.close_button.pack(side='right')
        # self.maximize_btn.pack(side=tk.RIGHT)
        self.minimize_btn.pack(side=tk.RIGHT)
        self.move_window_bindings(status=True)

    '''Functional Public Methods'''
    def get_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def loop_control(self):
        self.parent.update_idletasks()
        self.parent.withdraw()
        self.set_appwindow()

    def maximizeToggle(self, event=None):
        if self.maximized == False:
            self.winfo_update()
            #maximize current window
            self.maximize_btn.config(text="❐")
            hwnd = windll.user32.GetParent(self.parent.winfo_id())
            SWP_SHOWWINDOW = 0x40
            windll.user32.SetWindowPos(hwnd, 0, 0, 0, 
                int(self.parent.winfo_screenwidth()),
                int(self.parent.winfo_screenheight()-48),
                SWP_SHOWWINDOW)
            self.maximized = True
            self.move_window_bindings(status=False)
        else:
            #restore down window
            self.maximize_btn.config(text="🗖")
            hwnd = windll.user32.GetParent(self.parent.winfo_id())
            SWP_SHOWWINDOW = 0x40
            windll.user32.SetWindowPos(hwnd, 0, 
                self.previousPosition[0],
                self.previousPosition[1],
                int(self.parent.windowSize[0]),
                int(self.parent.windowSize[1]),
                SWP_SHOWWINDOW)
            self.maximized = False
            self.move_window_bindings(status=True)

    def minimize(self, hide=False):
       #reference: https://programtalk.com/python-examples/ctypes.windll.user32.ShowWindow/ 
        hwnd = windll.user32.GetParent(self.parent.winfo_id())
        windll.user32.ShowWindow(hwnd, 0 if hide else 6)

    def move_window(self, event):
        self.parent.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')
        self.previousPosition = [self.parent.winfo_x(), self.parent.winfo_y()]

    def move_window_bindings(self, *args, status=True):
        if status == True:
            self.title_bar.bind("<B1-Motion>", self.move_window)
            self.title_bar.bind("<Button-1>", self.get_pos)
            self.title_name.bind("<B1-Motion>", self.move_window)
            self.title_name.bind("<Button-1>", self.get_pos)
        else:
            self.title_bar.unbind("<B1-Motion>")
            self.title_bar.unbind("<Button-1>")
            self.title_name.unbind("<B1-Motion>")
            self.title_name.unbind("<Button-1>")

    def quit(self):
        self.parent.destroy()

    def set_appwindow(self):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        if not self.hasstyle:
            hwnd = windll.user32.GetParent(self.parent.winfo_id())
            style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
            self.parent.withdraw()
            self.parent.after(10, lambda:self.parent.wm_deiconify())
            self.hasstyle=True

    def winfo_update(self):
        """Update geometry() information, return None"""
        self.parent.windowSize = [self.parent.winfo_width(),
                                  self.parent.winfo_height()]