BGCOLOR = '#21325E'
CORRECT_COLOR = '#F1D00A'
WRONG_COLOR = '#3E497A'
BTN_COLOR = '#F0F0F0'

import tkinter as tk
from tkinter import *
from time import *
from PIL import ImageTk, Image
import random

#이미지 입력
#숫자선택


answer = 0 
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)
        master.title('Main Page')
        
        tk.Button(self, width=35, height=2, text='의무군인(징병제) 신체검사', font =('나눔바른펜', 15, 'bold'),command = lambda: master.switch_frame(Soldier_height),bg = CORRECT_COLOR).pack(pady = 10)
        tk.Button(self, width=35, height=2, text='직업군인 신체검사', font =('나눔바른펜', 15, 'bold'),command = lambda: master.switch_frame(Soldier_job),bg = CORRECT_COLOR).pack(pady = 10)
        tk.Button(self, width=35, height=2, text='경찰(경찰대학x) 신체검사', font =('나눔바른펜', 15, 'bold'),command = lambda: master.switch_frame(Police),bg = CORRECT_COLOR).pack(pady = 10)
        tk.Button(self, width=35, height=2, text='소방관 신체검사', font =('나눔바른펜', 15, 'bold'),command = lambda: master.switch_frame(Fire),bg = CORRECT_COLOR).pack(pady = 10)
        tk.Button(self, width=35, height=2, text='조종사 신체검사', font =('나눔바른펜', 15, 'bold'),command = lambda: master.switch_frame(Poilot),bg = CORRECT_COLOR).pack(pady = 10)
        tk.Button(self, width=35, height=2, text='공무원(교사, 9급, 7급) 신체검사', font =('나눔바른펜', 15, 'bold'),command = lambda: master.switch_frame(officer),bg = CORRECT_COLOR).pack(pady = 10)
        tk.Button(self, width=35, height=2, text='운전면허 신체검사', font =('나눔바른펜', 15, 'bold'),command = lambda: master.switch_frame(driver),bg = CORRECT_COLOR).pack(pady = 10)


class Soldier_height(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)
        img = '006.png'
        img = ImageTk.PhotoImage(Image.open("008.gif"))  
        l=Label(image=img)
        l.pack()
        tk.The_Entry = Entry(master)
        tk.The_Entry.pack()

class Soldier_weight(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class Soldier_key(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class Soldier_key(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class Soldier_key(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class Soldier_key(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

    

class Soldier_job(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class Police(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class Fire(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class Poilot(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class officer(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

class driver(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, padx = 30, pady = 10, bg = BGCOLOR)

app = SampleApp()
app.mainloop()      


