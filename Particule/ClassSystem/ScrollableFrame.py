import tkinter as tk
from tkinter import ttk
from Particule import *


class ScrollableFrame(ttk.Frame):
    def __init__(self, container,size, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self,width=size-25)

        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview, style='Vertical.TScrollbar')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.CanvasWin=self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row = 0, column = 0)#.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.grid(row = 0, column = 1,sticky = NE + SE)#.pack(anchor=E, side=RIGHT, fill=Y)

        self.canvas.bind('<Configure>', self.FrameWidth)

    def FrameWidth(self, event):

        canvas_width = event.width
        canvas_height = event.height
        self.canvas.itemconfig(self.CanvasWin,width=canvas_width)#,height=canvas_height)