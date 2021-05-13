from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
from ClassSystem.EditorWindow import EditorWindow

class Notebook(ttk.Notebook):
    def __init__(self,root,**kwargs):
        ttk.Notebook.__init__(self,root,**kwargs)
        self.Particule = root.Particule


    """def add(self, child, **kw):
        ttk.Notebook.add(self,child,**kw)
        if issubclass(type(child), EditorWindow):
            if not child in self.Particule.AllEditorWindow:
                self.Particule.AllEditorWindow.append(child)
        #print(self._w)
        #self.make_draggable()"""

    def OnFocus(self):
        pass

    def OnLostFocus(self):  # Messages
        pass
    """
    def make_draggable(self,widget):
        widget.bind("<Button-1>", self.on_drag_start)
        widget.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self,event):
        print("on_drag_start: ")
        print("widget event: ", event)
        print("widget: ", event.widget)
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def on_drag_motion(self,event):
        print("on_drag_motion: ")
        print("widget event: ", event)

        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        print("tuple: ", x, y)
        widget.place(x=x, y=y)
    """
