import tkinter as tk
from tkinter import ttk
from Particule import *
import platform

class ScrollableFrame(ttk.Frame):
    def __init__(self, container,size, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self,width=size-25)
        self.canvas.pack(side=LEFT, fill=tkinter.BOTH, expand=True, anchor=N)

        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview, style='Vertical.TScrollbar')
        self.scrollbar.pack(side=RIGHT,fill="y") # .pack(anchor=E, side=RIGHT, fill=Y)


        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.scrollable_frame.bind(
            '<Button-1>',
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.CanvasWin=self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")



        self.canvas.bind('<Configure>', self.FrameWidth)


    def FrameWidth(self, event):

        canvas_width = event.width
        canvas_height = event.height
        self.canvas.itemconfig(self.CanvasWin,width=canvas_width)#,height=canvas_height)

    def UpdateScroll(self):
        for i in range(3):
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))
            self.canvas.update()


    def OnDestroy(self):
        self.canvas.destroy()