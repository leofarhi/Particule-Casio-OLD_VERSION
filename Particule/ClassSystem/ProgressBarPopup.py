import tkinter as tk
import tkinter.ttk as ttk
class ProgressBarPopup(tk.Toplevel):
    def __init__(self, root, **kwargs):
        tk.Toplevel.__init__(self, root, **kwargs)
        self.attributes("-topmost", True)
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack()
    def SetValue(self,value):
        self.progress['value'] = value