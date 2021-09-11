import traceback
from VisualScratch import *
from ClassSystem.EditorWindow import EditorWindow

class Console(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self,RootWindow)
        self.listError = Listbox(self)
        self.listError.pack(fill=tkinter.BOTH, expand=True)
        self.LabelFrame = LabelFrame(self)
        self.LabelFrame.pack(fill=tkinter.X, expand=True)
        self.labelError = Text(self)
        self.labelError.configure(state='disabled')
        self.labelError.pack(fill=tkinter.BOTH, expand=True,anchor='nw')
        self.listError.bind("<<ListboxSelect>>", self.select)


        #tk.Tk.report_callback_exception = self.show_error

    def show_error(self, *args):
        err = traceback.format_exception(*args)
        elems = self.listError.get('@1,0', END)
        if len(elems)>20:
            self.listError.delete(0)
        self.listError.insert(END,err)
        #messagebox.showerror('Exception', err)

    def select(self,event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.setTextInput(data)
            #self.labelError.configure(text=data)

    def setTextInput(self, text):
        self.labelError.configure(state='normal')
        self.labelError.delete(1.0, "end")
        self.labelError.insert(1.0, text)
        self.labelError.configure(state='disabled')
