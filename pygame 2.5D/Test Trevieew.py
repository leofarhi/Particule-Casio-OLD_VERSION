import os
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class App(ttk.Frame):

    def __init__(self, master, path):

        ttk.Frame.__init__(self, master)
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Directory', anchor='w')

        root_node = self.tree.insert('', 'end', text='  Work Folder', open=True)
        l1_node = self.tree.insert(root_node, 'end', text='level 1', open=True)
        l2_node = self.tree.insert(l1_node, 'end', text='level 2', open=True)
        l3_node = self.tree.insert(l2_node, 'end', text='level 3', open=True)
        l2a_node = self.tree.insert(l1_node, 'end', text='level 2a', open=True)
        l3a_node = self.tree.insert(l2a_node, 'end', text='level 3a', open=True)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        self.grid()

root = tk.Tk()
path_to_my_project = os.getcwd()
app = App(root, path=path_to_my_project)
#app.mainloop()
