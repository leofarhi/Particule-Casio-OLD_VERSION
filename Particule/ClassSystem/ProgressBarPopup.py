import tkinter as tk
import tkinter.ttk as ttk
import platform
class ProgressBarPopup(tk.Toplevel):
    def __init__(self, root, **kwargs):
        if platform.system()=='Linux':return
        tk.Toplevel.__init__(self, root, **kwargs)
        self.attributes("-topmost", True)
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack()
    def SetValue(self,value):
        if platform.system() == 'Linux': return
        self.progress['value'] = value
    if platform.system() == 'Linux':
        def destroy(self):
            pass