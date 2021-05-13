import sys, os
from tkinter.filedialog import *
from tkinter import *

def open_file(rep=os.getcwd()):
    root = Tk ()
    #root.withdraw()
    root.filename = askopenfilename (initialdir = rep, title = "Select file" )#, filetypes = (( "jpeg files" , "* .jpg" ), ( "all files" , "* * . * " )))
    root.destroy()
    return root.filename
def open_files(rep=os.getcwd()):
    root = Tk ()
    #root.withdraw()
    root.filename = askopenfilenames (initialdir = rep, title = "Select file" )#, filetypes = (( "jpeg files" , "* .jpg" ), ( "all files" , "* * . * " )))
    root.destroy()
    return root.filename
def save_file(rep=os.getcwd()):
    root = Tk ()
    #root.withdraw()
    root.filename = asksaveasfilename (initialdir = rep , title = "Select file")# , filetypes = (( "jpeg files" , "* .jpg" ), ( "all files" , "* * . * " )))
    root.destroy()
    return root.filename

def open_folder(rep=os.getcwd()):
    root = Tk ()
    #root.withdraw()
    root.directory = askdirectory(initialdir = rep , title = "Select folder")
    root.destroy()
    return root.directory
