from Particule import *
def LoadingProgressPourcent(nb):
    global Loadingprogress, LoadingProgressWindow
    Loadingprogress['value'] = nb
    LoadingProgressWindow.update_idletasks()

def LoadingProgress(texte):
    global Loadingprogress, LoadingProgressWindow
    LoadingProgressWindow = Toplevel(self.Mafentre)
    LoadingProgressWindow.title("Loading")
    lb = Label(LoadingProgressWindow, text=texte)
    lb.pack()
    Loadingprogress = ttk.Progressbar(LoadingProgressWindow, orient=HORIZONTAL,
                                      length=100, mode='determinate')
    LoadingProgressPourcent(1)
    Loadingprogress.pack(pady=10)