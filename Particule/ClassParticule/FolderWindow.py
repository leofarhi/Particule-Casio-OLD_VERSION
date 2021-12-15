#https://github.com/RainingComputers/whipFTP/blob/master/whipFTP.py
from Particule import *
from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
import tkinter as tk
import time
from stat import ST_MTIME
from time import localtime, asctime
from os import stat
from ClassSystem.EditorWindow import EditorWindow
from ClassParticule.Texture import Texture
import tkinter as tk
from tkinter import simpledialog
from tkinter.messagebox import askyesno
import psutil
import pyperclip
from ClassParticule.FileVariable import FileVariable
import platform

class FolderWindow(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self, RootWindow, Resize=True, ScrollbarShow=False)

        self.TextureVide = Texture(self.Particule,name="None",UUID = "TextureVide")
        self.TextureVide.name = "TextureVide"

        # Cell width of each cell
        self.cell_width = 190
        self.cell_height = 70

        # List to store all item names (including folders) that are currently being displayed and their details
        self.file_list = []
        self.detailed_file_list = []
        # An index that points to current file that the mouse is pointing
        self.current_file_index = 0

        # Variables for drawing and storing cursor position
        self.mouse_x = 0
        self.mouse_y = 0
        self.max_width = 0

        # Variable to store which cell cursor is currently pointing
        self.x_cell_pos = 0
        self.y_cell_pos = 0

        # A dictionary to store indices and highlight rectangle references of selected files
        self.selected_file_indices = {}

        # A list to hold files that have been droped into the window
        self.dnd_file_list = []

        # Things in the clipboard
        self.cut = False
        self.copy = False
        self.clipboard_file_list = []
        self.clipboard_path_list = []
        self.detailed_clipboard_file_list = []

        # Variable to store start cell position of drag select
        self.start_x = 0
        self.start_y = 0

        # Variable to tell weather to change status, if false the current message will stay on status bar and status bar will ignore other status messages
        self.change_status = True

        # Variable to tell replace all has been selected
        self.replace_all = False

        # Variable to tell skip all has been selected
        self.skip_all = False

        # Variable to tell weather a search has been performes
        self.search_performed = False

        # Variable to tell weather hidden file are enabled
        self.hidden_files = False

        # Variable to tell a thread weather to replace a file
        self.replace_flag = False


        # Variable to tell weather to displat updatin file list dialog
        self.float_dialog_destroy = False


        # Create frame for toolbar buttons
        self.toolbar = ttk.Frame(self)
        self.toolbar.pack(fill=X)

        # Create frame for text fields
        self.entry_bar = ttk.Frame(self)
        self.entry_bar.pack(fill=X)

        # Create frame for canvas and scrollbar
        self.pad_frame = ttk.Frame(self)
        self.pad_frame.pack(fill=BOTH, expand=True)
        self.canvas_frame = ttk.Frame(self.pad_frame, relief='groove', border=1)
        self.canvas_frame.pack(fill=BOTH, expand=True, padx=5, pady=3)


        # Variables to kepp track of wain frame and animation
        self.wait_anim = False
        self.wait_frame_index = 1
        self.continue_wait = False

        # Load all icons
        self.connect_icon = PhotoImage(file='lib/Icons/connect_big.png')
        self.upload_icon = PhotoImage(file='lib/Icons/upload_big.png')
        self.download_icon = PhotoImage(file='lib/Icons/download_big.png')
        self.newfolder_icon = PhotoImage(file='lib/Icons/newfolder_big.png')
        self.up_icon = PhotoImage(file='lib/Icons/up_big.png')
        self.info_icon = PhotoImage(file='lib/Icons/info_big.png')
        self.delete_icon = PhotoImage(file='lib/Icons/delete_big.png')
        self.properties_icon = PhotoImage(file='lib/Icons/properties_big.png')
        self.cut_icon = PhotoImage(file='lib/Icons/cut_big.png')
        self.copy_icon = PhotoImage(file='lib/Icons/copy_big.png')
        self.paste_icon = PhotoImage(file='lib/Icons/paste_big.png')
        self.permissions_icon = PhotoImage(file='lib/Icons/permissions_big.png')
        self.folder_icon = PhotoImage(file='lib/Icons/folder_big.png')
        self.textfile_icon = PhotoImage(file='lib/Icons/textfile_big.png')
        self.console_icon = PhotoImage(file='lib/Icons/console_big.png')
        self.search_icon = PhotoImage(file='lib/Icons/search_big.png')
        self.rename_icon = PhotoImage(file='lib/Icons/rename_big.png')
        self.whipFTP_icon = PhotoImage(file='lib/Icons/whipFTP_large.png')
        self.goto_icon = PhotoImage(file='lib/Icons/gotopath_big.png')

        self.Picturefile_icon = PhotoImage(file='lib/Icons/picture.png')
        self.VisualScratchfile_icon = PhotoImage(file='lib/Icons/VisualScratch.png')
        self.Scenefile_icon = PhotoImage(file='lib/Icons/SceneFile.png')
        self.PrefabFile_icon = PhotoImage(file='lib/Icons/PrefabFile.png')

        # Load glow version of icons
        self.connect_glow_icon = PhotoImage(file='lib/Icons_glow/connect_big_glow.png')
        self.upload_glow_icon = PhotoImage(file='lib/Icons_glow/upload_big_glow.png')
        self.download_glow_icon = PhotoImage(file='lib/Icons_glow/download_big_glow.png')
        self.newfolder_glow_icon = PhotoImage(file='lib/Icons_glow/newfolder_big_glow.png')
        self.up_glow_icon = PhotoImage(file='lib/Icons_glow/up_big_glow.png')
        self.info_glow_icon = PhotoImage(file='lib/Icons_glow/info_big_glow.png')
        self.delete_glow_icon = PhotoImage(file='lib/Icons_glow/delete_big_glow.png')
        self.properties_glow_icon = PhotoImage(file='lib/Icons_glow/properties_big_glow.png')
        self.cut_glow_icon = PhotoImage(file='lib/Icons_glow/cut_big_glow.png')
        self.copy_glow_icon = PhotoImage(file='lib/Icons_glow/copy_big_glow.png')
        self.paste_glow_icon = PhotoImage(file='lib/Icons_glow/paste_big_glow.png')
        self.console_glow_icon = PhotoImage(file='lib/Icons_glow/console_big_glow.png')
        self.search_glow_icon = PhotoImage(file='lib/Icons_glow/search_big_glow.png')
        self.whipFTP_glow_icon = PhotoImage(file='lib/Icons_glow/whipFTP_large_glow.png')
        self.dnd_glow_icon = PhotoImage(file='lib/Icons_glow/upload_large_glow.png')
        self.goto_glow_icon = PhotoImage(file='lib/Icons_glow/gotopath_big_glow.png')

        # Load icons from the wait animations
        self.wait_frames = []
        self.wait_frames.append(PhotoImage(file='lib/Icons_glow/wait_anim_frame_one.png'))
        self.wait_frames.append(PhotoImage(file='lib/Icons_glow/wait_anim_frame_two.png'))
        self.wait_frames.append(PhotoImage(file='lib/Icons_glow/wait_anim_frame_three.png'))
        self.wait_frames.append(PhotoImage(file='lib/Icons_glow/wait_anim_frame_four.png'))
        self.problem_icon = PhotoImage(file='lib/Icons_glow/problem.png')

        # Create scrollbar
        self.vbar = ttk.Scrollbar(self.canvas_frame, orient=VERTICAL, style='Vertical.TScrollbar')
        self.vbar.pack(anchor=E, side=RIGHT, fill=Y)
        # Create drawing space for all file and folder icons
        self.canvas = Canvas(self.canvas_frame, relief='flat', bg='white', highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.vbar.config(command=self.canvas.yview)
        self.canvas['yscrollcommand'] = self.vbar.set
        # Create status text/bar and status sting viraiable
        self.current_status = StringVar()
        self.status_label = ttk.Label(self, textvariable=self.current_status, anchor='center')
        self.status_label.pack(fill=X)

        #Drag System
        self.mitem = tkinter.Toplevel(self)
        self.mitem.canvasDrag = Canvas(self.mitem, width=32, height=32)
        self.mitem.canvasDrag.pack(expand=True, fill=BOTH)
        self.mitem.canvasDrag.create_image(16, 16, image=self.folder_icon)
        self.mitem.overrideredirect(1)
        self.mitem.config(bg="white")
        self.mitem.withdraw()
        self.DropFile=None


        # Bind events
        self.bind_events()

    def bind_events(self):
        # Bind keyboard shortcuts
        """self.bind('<Control-h>', self.toggle_hidden_files)
        self.bind('<Control-H>', self.toggle_hidden_files)
        self.bind('<Control-c>', self.clipboard_copy)
        self.bind('<Control-C>', self.clipboard_copy)
        self.bind('<Control-x>', self.clipboard_cut)
        self.bind('<Control-X>', self.clipboard_cut)
        self.bind('<Control-v>', self.clipboard_paste_thread_create)
        self.bind('<Control-V>', self.clipboard_paste_thread_create)
        self.bind('<Delete>', self.delete_window)"""

        # Bind events for canvas, this part of code tells what some of the functions do
        self.canvas.bind('<Button-4>', self.on_mouse_wheel)
        self.canvas.bind('<Button-5>', self.on_mouse_wheel)
        self.canvas.bind('<MouseWheel>', self.on_mouse_wheel)
        self.canvas.bind('<Configure>', self.draw_icons)
        self.canvas.bind('<Motion>', self.update_status_and_mouse)
        self.canvas.bind('<Button-1>', self.mouse_select)
        self.canvas.bind('<Double-Button-1>', self.change_dir)
        self.canvas.bind('<Control-Button-1>', self.ctrl_select)
        self.canvas.bind("<ButtonRelease-1>", self.mouserelease)
        self.canvas.bind('<B1-Motion>', self.drag_select)

        # Bind events for statusbar and scroll bar
        self.vbar.bind('<Motion>', lambda event, arg='Scrollbar.': self.update_status(event, arg))
        self.status_label.bind('<Motion>', lambda event, arg='Statusbar.': self.update_status(event, arg))

        self.nameFilereturn = "<---"
        self.repertoirSlc = self.Particule.FolderProject+"/Assets"

        self.CreateMetaFile()
        self.GetAll_UUID()
        self.update_search_files()

        self.canvas.bind("<Button-3>", self.popup)
        self.contextMenu = Menu(self.Particule.Mafenetre, tearoff=False)
        #self.contextMenu.add_command(label="Copy")
        #self.contextMenu.add_command(label="Past")
        #self.contextMenu.add_separator()
        self.CreateMenu = Menu(self.Particule.Mafenetre, tearoff=False)
        self.contextMenu.add_cascade(label= TradTxt("Creer"),menu=self.CreateMenu)
        self.CreateMenu.add_command(label=TradTxt("Scratch Script"),command=self.CreateScratchScript)
        self.CreateMenu.add_separator()
        self.CreateMenu.add_command(label=TradTxt("Dossier"), command=self.create_dir)

        self.contextMenu.add_separator()
        self.contextMenu.add_command(label=TradTxt("Renommer"),command=self.RenameFile)
        #self.contextMenu.add_command(label="Duplicate")
        self.contextMenu.add_command(label=TradTxt("Supprimer"), command=self.Destroy)


    def Destroy(self,*args):
        try:
            file = self.detailed_file_list[self.current_file_index]
        except:
            return
        if (os.path.basename(file)=="<---"):
            return
        valid = askyesno(title='confirmation',
                    message=TradTxt('etes-vous sur de vouloir supprimer "')+os.path.basename(file)+'" ?')
        if valid:
            if (os.path.isfile(file)):
                os.remove(file)
            else:
                shutil.rmtree(file)
            self.Particule.UpdateOnFocus()

    def CreateScratchScript(self,*args):
        name = simpledialog.askstring(title=TradTxt("Nom de fichier"),
                               prompt=TradTxt("Quel est le nom de la Class ?"))
        if name==None:
            return
        fileName = self.repertoirSlc + "/" + name +".SBAsset"
        with open(fileName,"w") as fic:
            fic.write("""AllWidget::[[100, 100, 'Forme0', [None], None, [['Label', None]], 'InEditor', [['Label', "Dans l'Editeur"]], []]]""")
        self.Particule.UpdateOnFocus()

    def popup(self, event):
        """action in event of button 3 on tree view"""
        self.contextMenu.post(event.x_root, event.y_root)

    def mouserelease(self, event):
        self.mitem.withdraw()
        if len(self.selected_file_indices)>0:
            if (self.current_file_index >= 0 and self.current_file_index < len(
                    self.file_list) and self.mouse_x < self.max_width):
                if os.path.splitext(self.file_list[self.current_file_index])[1] in [".png", ".jpg", ".bmp"]:
                    self.Particule.ScreenOrganization.ChangeInspector("Image")
            else:
                if os.path.splitext(self.detailed_file_list[list(self.selected_file_indices)[0]])[1] in [".png", ".jpg", ".bmp"]:
                    texture=None
                    try:
                        path = self.detailed_file_list[list(self.selected_file_indices)[0]]
                        guid = rf.found(path + ".meta", "guid")
                        #texture = Texture(self.Particule, Path=self.Particule.FolderProject + "/Library/ImagesBmpCache/" +guid+'.bmp',
                        #                  name=os.path.basename(self.detailed_file_list[list(self.selected_file_indices)[0]]))
                    except:pass
        if self.DropFile!=None:
            self.Drop_item(event)
        #print(str(len(self.file_list)) + '   Selected: ' + str(len(self.selected_file_indices)) )
        #print(self.selected_file_indices)
        #print(self.repertoirSlc +"/"+self.detailed_file_list[list(self.selected_file_indices)[0]])

    def Drop_item(self,event):
        #print(self.DropFile)
        mouse_x, mouse_y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        x_cell_pos = int(mouse_x / self.cell_width)
        y_cell_pos = int(mouse_y / self.cell_height)
        max_width = self.canvas_width - (self.canvas_width % self.cell_width)
        current_file_index = int(((max_width / self.cell_width) * y_cell_pos) + x_cell_pos)
        if (current_file_index >= 0 and current_file_index < len(self.file_list) and mouse_x < max_width):
            slc = self.detailed_file_list[current_file_index]
            #print(slc)
            if self.is_dir(slc) and (not slc in self.DropFile):
                for i in self.DropFile:
                    if self.repertoirSlc +"/"+self.nameFilereturn==slc:
                        shutil.move(i, os.path.dirname(self.repertoirSlc) +"/"+os.path.basename(i))
                        shutil.move(i+".meta", os.path.dirname(self.repertoirSlc) + "/" + os.path.basename(i)+".meta")
                    else:
                        shutil.move(i, slc + "/" + os.path.basename(i))
                        shutil.move(i + ".meta", slc + "/" + os.path.basename(i) + ".meta")
        self.DropFile = None
        self.CreateMetaFile()
        self.GetAll_UUID()
        self.Particule.SLN_System.UpdateSLN()
        self.update_search_files()

    def GetAll_UUID(self,rep=None):
        if rep == None:
            rep = self.Particule.FolderProject
        lst = os.listdir(rep)
        AllFileVariable=[]
        for i in lst:
            if ".meta" in i and os.path.isfile(rep + "/" + i):
                TempID=rf.found(rep + "/" + i,"guid")
                if TempID in list(self.Particule.All_UUID.keys()):
                    UUID = TempID
                else:
                    fv = FileVariable(self.Particule, rep + "/" + i, TempID)
                    if TempID==None:
                        TempID = fv.ID
                    UUID = self.Particule.CreateUUID(fv,TempID)
                    AllFileVariable.append(fv)
                    #fv.UpdateCheck()
                rf.save(rep + "/" + i, "guid", UUID)
                org = os.path.splitext(i)[0]
                if os.path.splitext(org)[1] == ".particule":
                    rf.save(rep + "/" + i, "UUID_In_Scene",self.Particule.SaveData.GetAll_UUID_Scene(rep + "/" +org))
            if not os.path.isfile(rep+"/"+i):
                self.GetAll_UUID(rep+"/"+i)
        for i in AllFileVariable:
            i.UpdateCheck()
    def CreateMetaFile(self,rep=None):
        if rep == None:
            rep = self.Particule.FolderProject
        lst = os.listdir(rep)
        for i in lst:
            if ".meta" == os.path.splitext(i)[1] and os.path.isfile(rep+"/"+i):
                if os.path.splitext(i)[0] in lst:
                    continue
                else:
                    os.remove(rep + "/" + i)
                    continue
            if not os.path.isfile(rep+"/"+i):
                self.CreateMetaFile(rep+"/"+i)
            if not i+".meta" in lst:
                with open(rep+"/"+i+".meta","w") as fic:
                    fic.write("")

            pathFile = rep+"/"+i
            pathMeta = rep + "/" + i + ".meta"
            Date = rf.found(pathMeta,"Date")
            IsHide = rf.found(pathMeta, "IsHide")
            infos = stat(pathFile)
            fileDate = asctime(localtime(infos[ST_MTIME]))
            if fileDate != Date:
                rf.save(pathMeta,"Date",fileDate)
                pass#Update this
            if IsHide==None:
                rf.save(pathMeta, "IsHide", False)
            rf.save(pathMeta, "pathFile", pathFile)




    def update_file_list(self):
        # Disable toolbar
        self.start_wait()
        # Set search to false
        self.search_performed = False
        self.unlock_status_bar()
        self.update_search_files()
        self.end_wait()
    def is_dir(self,path):
        if path==self.repertoirSlc +"/"+self.nameFilereturn:
            return True
        return not os.path.isfile(path)

    def SelectIconWithExtention(self,file):
        if os.path.isdir(file):
            return self.folder_icon
        ext= os.path.splitext(file)[1]
        if ext in [".bmp",".png",".jpeg",".jpg"]:
            return self.Picturefile_icon
        elif ext == ".SBAsset":
            return self.VisualScratchfile_icon
        elif ext == ".particule":
            return self.Scenefile_icon
        elif ext == ".prefab":
            return self.PrefabFile_icon
        return self.textfile_icon
    def draw_icons(self, event=None):
        # Calculate cell width
        self.cell_width = 80
        self.canvas_width = self.canvas.winfo_width() - 4
        self.canvas_height = self.canvas.winfo_height()
        if (self.cell_width > self.canvas_width):
            self.cell_width = self.canvas_width
        # Clear canvas
        self.canvas.delete('all')
        y = 0
        x = 0
        # Create a rectangle for update_status_mouse(self, event) function
        self.rect_id = self.canvas.create_rectangle(-1, -1, -1, -1, fill='', outline='')
        # Draw icons
        # If there are no files, draw watermark
        if len(self.file_list) is 0:
            self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.whipFTP_glow_icon)
        for file_name, file_details in zip(self.file_list, self.detailed_file_list):
            if ((x + 1) * self.cell_width > self.canvas_width):
                y += 1
                x = 0

            # Check types, draw appropriate icon
            if (self.is_dir(file_details)):
                if len(file_name) > 8:
                    file_name = file_name[:8] + "..."
                self.canvas.create_image(25 + (x * self.cell_width), 18 + (y * self.cell_height), image=self.folder_icon)
                #canvas_id = self.canvas.create_text(45 + (x * self.cell_width), 13 + (y * 35), anchor='nw')
                canvas_id = self.canvas.create_text(0 + (x * self.cell_width), 45 + (y * self.cell_height), anchor='nw')
                self.canvas.itemconfig(canvas_id, text=file_name)
                x += 1
            else:
                file_name = file_name.split(".")[0]
                if len(file_name) > 8:
                    file_name = file_name[:8] + "..."
                self.canvas.create_image(25 + (x * self.cell_width), 18 + (y * self.cell_height), image=self.SelectIconWithExtention(file_details))
                #canvas_id = self.canvas.create_text(45 + (x * self.cell_width), 13 + (y * 35), anchor='nw')
                canvas_id = self.canvas.create_text(0 + (x * self.cell_width), 45 + (y * self.cell_height), anchor='nw')
                self.canvas.itemconfig(canvas_id, text=file_name)
                x += 1
        # Calculate scroll region for scroll bar
        if (y + 1) * self.cell_height < self.canvas_height:
            scroll_region_y = self.canvas_height - 1
            self.vbar.bind('<Motion>', lambda event, arg='': self.update_status(event, arg))
        else:
            scroll_region_y = ((y + 1) * self.cell_height) + 13
            self.vbar.configure(style='TScrollbar')
            self.vbar.bind('<Motion>', lambda event, arg='Scrollbar.': self.update_status(event, arg))
        self.canvas.configure(scrollregion='-1 -1 ' + str(self.canvas_width) + ' ' + str(scroll_region_y))
        # Redraw all selected-highlight rectangles for selected files
        for file_index in self.selected_file_indices:
            # Round canvas's width to nearest multiple of self.cell_width, width of each cell
            self.max_width = self.canvas_width - (self.canvas_width % self.cell_width)
            max_no_cells_x = self.max_width / self.cell_width
            x = file_index % max_no_cells_x
            y = int(file_index / max_no_cells_x)
            self.selected_file_indices[file_index] = self.canvas.create_rectangle(x * self.cell_width + 2, y * self.cell_height + 2,
                                                                                  (x + 1) * self.cell_width - 1,
                                                                                  (y + 1) * self.cell_height - 1, fill='',
                                                                                  outline='Red')

    def update_status_and_mouse(self, event):
        # Get absolute mouse position on canvas
        self.mouse_x, self.mouse_y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        # Calculate cell row and cell column based on mouse's position
        self.x_cell_pos = int(self.mouse_x / self.cell_width)
        self.y_cell_pos = int(self.mouse_y / self.cell_height)
        # Round canvas's width to nearest multiple of self.cell_width, width of each cell
        self.max_width = self.canvas_width - (self.canvas_width % self.cell_width)
        # Use index = (y*width)+x to figure out the file index from canvas and mouse position
        self.current_file_index = int(((self.max_width / self.cell_width) * self.y_cell_pos) + self.x_cell_pos)
        # Set status only if valid index, draw mouse-hover highlight rectangle
        if (self.current_file_index >= 0 and self.current_file_index < len(
                self.file_list) and self.mouse_x < self.max_width):
            self.update_status(event, self.detailed_file_list[self.current_file_index])
            # Configure the rectangle created in draw_icons() to highlight the current folder mose is pointing at
            self.canvas.itemconfig(self.rect_id, outline='black')
            self.canvas.coords(self.rect_id, self.x_cell_pos * self.cell_width + 2 -(self.cell_width//4), self.y_cell_pos * self.cell_height + 2,
                               (self.x_cell_pos + 1) * self.cell_width - 1 -(self.cell_width//4), (self.y_cell_pos + 1) * self.cell_height - 1)
        else:
            # Tell how many files are present and how many are selected in the status bar
            self.update_status(event, 'Total no. of items: ' + str(len(self.file_list)) + '   Selected: ' + str(
                len(self.selected_file_indices)))
            # Stop mouse-hover highlighting
            self.canvas.itemconfig(self.rect_id, outline='')
            self.canvas.coords(self.rect_id, -1, -1, -1, -1)

    def update_status(self, event=None, message=' '):
        # Stop mouse-hover highlighting
        self.canvas.itemconfig(self.rect_id, outline='')
        self.canvas.coords(self.rect_id, -1, -1, -1, -1)
        # Display message in status bar in black color only if change_status is true else ignore it
        if self.change_status is True:
            self.status_label.configure(style='TLabel')
            self.current_status.set(message)

    def update_status_red(self, message):
        # Stop mouse-hover highlighting
        self.canvas.itemconfig(self.rect_id, outline='')
        self.canvas.coords(self.rect_id, -1, -1, -1, -1)
        # Display message in status bar in red color only if change_status is true else ignore it
        if self.change_status is True:
            self.status_label.configure(style='Red.TLabel')
            self.current_status.set(message)
            self.problem()

    def lock_status_bar(self):
        self.change_status = False

    def unlock_status_bar(self):
        self.change_status = True

    def toggle_hidden_files(self, event):
        self.ftpController.toggle_hidden_files()
        self.update_file_list()
        self.deselect_everything()

    def on_mouse_wheel(self, event):
        def delta(event):
            if event.num == 5 or event.delta < 0:
                return 1
            return -1

        self.canvas.yview_scroll(delta(event), 'units')

    def mouse_select(self, event):
        self.focus()
        # Store start position for drag select
        self.start_x = self.x_cell_pos
        self.start_y = self.y_cell_pos
        # Deselect everything
        self.deselect_everything()
        # Set selected only if valid index
        if (self.current_file_index >= 0 and self.current_file_index < len(
                self.file_list) and self.mouse_x < self.max_width):
            # Draw a 'selected' highlighting rectangle and save a reference to the rectangle in selected file list
            self.selected_file_indices[self.current_file_index] = self.canvas.create_rectangle(
                self.x_cell_pos * self.cell_width + 2 -(self.cell_width//4), self.y_cell_pos * self.cell_height + 2,
                (self.x_cell_pos + 1) * self.cell_width - 1 -(self.cell_width//4), (self.y_cell_pos + 1) * 70 - 1,
                fill='', outline='Red')
        # Tell how many files are present and how many are selected in the status bar
        self.update_status(event, 'Total no. of items: ' + str(len(self.file_list)) + '   Selected: ' + str(
            len(self.selected_file_indices)))

    def ctrl_select(self, event):
        # Set selected only if valid index
        if (self.current_file_index >= 0 and self.current_file_index < len(
                self.file_list) and self.mouse_x < self.max_width):
            # If WAS NOT selected already
            if (self.current_file_index not in self.selected_file_indices):
                # Draw a 'selected' highlighting rectangle and save a reference to the rectangle in selected file list
                self.selected_file_indices[self.current_file_index] = self.canvas.create_rectangle(
                self.x_cell_pos * self.cell_width + 2 -(self.cell_width//4), self.y_cell_pos * self.cell_height + 2,
                (self.x_cell_pos + 1) * self.cell_width - 1 -(self.cell_width//4), (self.y_cell_pos + 1) * 70 - 1,
                fill='', outline='Red')
            # If WAS selected already
            else:
                # Remove from selected file list
                del self.selected_file_indices[self.current_file_index]
                # Redraw icons
                self.draw_icons()
                # Tell how many files are present and how many are selected in the status bar
        self.update_status(event, 'Total no. of items: ' + str(len(self.file_list)) + '   Selected: ' + str(
            len(self.selected_file_indices)))

    def drag_select(self, event):
        # Update to get current mouse position
        #self.update_status_and_mouse(event)
        #self.t = event.widget
        #n = self.t.selection()
        #self.moveitem.set(self.t.focus())
        try:
            file = self.detailed_file_list[self.current_file_index]
        except:
            return
        self.mitem.canvasDrag.itemconfig(1,image =self.SelectIconWithExtention(file))
        x = self.Particule.Mafenetre.winfo_pointerx()
        y = self.Particule.Mafenetre.winfo_pointery()
        self.mitem.geometry("%dx%d+%d+%d" % (32, 32, x, y))
        self.mitem.deiconify()
        self.DropFile=[file]
        #self.t['cursor'] = "hand2"
        return
        # Calculate steps and offsets for x-direction
        if (self.x_cell_pos <= self.start_x):
            start_x_offset = 1
            step_x = 1
        else:
            start_x_offset = -1
            step_x = -1
        # Calculate steps and offsets for y-direction
        if (self.y_cell_pos <= self.start_y):
            start_y_offset = 1
            step_y = 1
        else:
            start_y_offset = -1
            step_y = -1
        # Select items
        for i in range(self.x_cell_pos, self.start_x + start_x_offset, step_x):
            for j in range(self.y_cell_pos, self.start_y + start_y_offset, step_y):
                # Calculate index
                file_index = int(((self.max_width / self.cell_width) * j) + i)
                # Set selected only if valid index
                if (file_index >= 0 and file_index < len(self.file_list) and i < self.max_width / self.cell_width):
                    # Draw a 'selected' highlighting rectangle and save a reference to the rectangle in selected file dictionary
                    self.selected_file_indices[file_index] = self.canvas.create_rectangle(i * self.cell_width + 2,
                                                                                          j * self.cell_height + 2,
                                                                                          (i + 1) * self.cell_width - 1,
                                                                                          (j + 1) * self.cell_height - 1, fill='',
                                                                                          outline='Red')

    def create_dir(self,*args):
        name = simpledialog.askstring(title=TradTxt("Nom du dossier"),
                                      prompt=TradTxt("Quel est le nom du dossier"))
        if name == None:
            return
        M.create_rep(self.repertoirSlc+"/"+name)
        self.Particule.UpdateOnFocus()
    def show_dnd_icon(self, action, actions, type, win, X, Y, x, y, data):
        # If there is another child window, disable dnd
        if (len(self.children) != 4): return
        self.deselect_everything()
        self.canvas.delete("all")
        self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.dnd_glow_icon)

    def deselect_everything(self):
        # Delete selected file dictionary
        self.selected_file_indices.clear()
        # Redraw all icons and remove any 'selected' highlighting rectangles
        self.draw_icons()

    def change_dir(self, event):
        # Delete selected file list
        self.selected_file_indices.clear()
        # Show message box
        if (self.current_file_index >= 0 and self.current_file_index < len(
                self.file_list) and self.mouse_x < self.max_width):

            if (self.is_dir(self.detailed_file_list[self.current_file_index])):
                    #try:
                    if self.detailed_file_list[self.current_file_index] == self.repertoirSlc+"/"+self.nameFilereturn:
                        self.repertoirSlc = os.path.abspath(os.path.join(self.repertoirSlc, os.pardir)).replace("\\", "/")
                    else:
                        self.repertoirSlc = self.detailed_file_list[self.current_file_index]
                    self.update_file_list()
                    """
                    except:
                        self.update_status_red('Unable to open directory, try reconnecting.')
                        self.lock_status_bar()
                    """
            else:
                if self.file_list[self.current_file_index].split(".")[-1] == "particule":
                    self.Particule.SaveData.LoadScene(self.detailed_file_list[self.current_file_index])
                if self.file_list[self.current_file_index].split(".")[-1] == "SBAsset":
                    if platform.system()=='Windows':
                        if not "main.exe" in (i.name() for i in psutil.process_iter()):
                            subprocess.Popen([self.Particule.VisualScratchPath, self.Particule.FolderProject + '/SLN/Solution.sls'])
                    elif platform.system() == 'Linux':
                        subprocess.Popen(["python", self.Particule.VisualScratchPath, self.Particule.FolderProject + '/SLN/Solution.sls'])
                if self.file_list[self.current_file_index].split(".")[-1] == "prefab":
                    valid = askyesno(title='confirmation',
                                     message=TradTxt('etes-vous sur de vouloir ajouter cette prefab ? '))
                    if valid:
                        path = self.detailed_file_list[self.current_file_index]
                        with open(path,"r") as fic:
                            pyperclip.copy(fic.read())
                            self.Particule.Hierarchy.PastObject()
    """
    def file_properties_window(self):
        # Check number of files selected
        if (len(self.selected_file_indices) is not 1): return
        # Create the string that contains all the properties
        for key in self.selected_file_indices:
            file_details = self.ftpController.get_properties(self.detailed_file_list[key])
            # Get file name
            file_name = file_details[0] + '\n'
            # Get file attributes
            file_attribs = file_details[1] + '\n'
            # Get date modified
            date_modified = file_details[2]
            if (self.ftpController.is_dir(self.detailed_file_list[key])):
                properties = 'Name: ' + file_name + 'Attributes: ' + file_attribs + 'Date: ' + date_modified
            else:
                file_size = file_details[3] + ' bytes'
                properties = 'Name: ' + file_name + 'Attributes: ' + file_attribs + 'Date: ' + date_modified + '\n' + 'Size: ' + file_size
        # Display the created string in properties dialog
        self.properties_dialog = Filedialogs.file_properties_dialog(self, 'Properties', self.rename_window,
                                                                    self.change_permissions_window,
                                                                    self.properties_icon, properties)
    
    def rename_window(self):
        self.properties_dialog.destroy()
        self.rename_dialog = Filedialogs.name_dialog(self, 'Rename', self.rename_file_thread, self.rename_icon)


    def search_window_ask(self):
        self.search_window = Filedialogs.name_dialog(self, 'Search', self.search_thread, self.search_icon,
                                                     'Enter file name:')
    """

    def RenameFile(self):
        try:
            file = self.detailed_file_list[self.current_file_index]
        except:
            return
        if not os.path.exists(file):return
        name = simpledialog.askstring(title=TradTxt("Renommer"),
                                      prompt=TradTxt("Quel est le nouveau nom de ")+os.path.basename(file))
        directory =os.path.dirname(file)
        ext = os.path.splitext(os.path.basename(file))[1]
        if name == None:
            return
        newfile = directory+"/"+name+ext

        os.rename(file, newfile)
        os.rename(file+".meta", newfile+".meta")
        rf.save(newfile + ".meta", "pathFile", newfile)

    def update_search_files(self):
        # Replace file lists with search results and redraw icons
        del self.file_list[:]
        del self.detailed_file_list[:]
        self.file_list = [i for i in os.listdir(self.repertoirSlc) if not ".meta" in i]
        self.detailed_file_list = [self.repertoirSlc+"/"+i for i in os.listdir(self.repertoirSlc) if not ".meta" in i]
        if self.repertoirSlc != self.Particule.FolderProject+"/Assets":
            self.file_list.insert(0, self.nameFilereturn)
            self.detailed_file_list.insert(0, self.repertoirSlc+"/"+self.nameFilereturn)
        self.draw_icons()

    """
    def delete_window(self, event=None):
        if (len(self.selected_file_indices) < 1): return
        self.delete_warning = Filedialogs.warning_dialog(self, 'Are you sure?', self.delete_thread,
                                                         self.delete_icon, 'Delete selected files/folders?')

    
    def clipboard_cut(self, event=None):
        # Check number of files in clipboard
        if (len(self.selected_file_indices) < 1): return
        self.cut = True
        del self.clipboard_file_list[:]
        for index in self.selected_file_indices:
            # If it is a search result get the clipboard path from the search result
            if (self.search_performed is True):
                self.clipboard_path_list.append('/'.join(self.file_list[index].split('/')[:-1]))
                self.clipboard_file_list.append(''.join(self.file_list[index].split('/')[-1:]))
            else:
                self.clipboard_path_list.append(self.ftpController.pwd())
                self.clipboard_file_list.append(self.file_list[index])
            self.detailed_clipboard_file_list.append(self.detailed_file_list[index])
        self.deselect_everything()

    def clipboard_copy(self, event=None):
        # Check number of files in clipboard
        if (len(self.selected_file_indices) < 1): return
        self.copy = True
        del self.clipboard_file_list[:]
        for index in self.selected_file_indices:
            # If it is a search result get the clipboard path from the search result
            if (self.search_performed is True):
                self.clipboard_path_list.append('/'.join(self.file_list[index].split('/')[:-1]))
                self.clipboard_file_list.append(''.join(self.file_list[index].split('/')[-1:]))
            else:
                self.clipboard_path_list.append(self.ftpController.pwd())
                self.clipboard_file_list.append(self.file_list[index])
            self.detailed_clipboard_file_list.append(self.detailed_file_list[index])
        self.deselect_everything()
    

    def clear_clipboard(self):
        del self.clipboard_file_list[:]
        del self.detailed_clipboard_file_list[:]
        del self.clipboard_path_list[:]
        self.cut = False
        self.copy = False

    def ask_replace(self, file_name, status):
        # Check if replace all has been selected
        if (self.replace_all is True): return True
        # Check if skip all has been selected
        if (self.skip_all is True): return False
        # Create replace dialog
        self.replace_window = Filedialogs.replace_dialog(self.console_window.console_dialog_window, 'Conflicting files',
                                                         self.copy_icon, file_name + ': ' + status + ', Replace?')
        # Loop till a button is pressed
        while self.replace_window.command is '':
            self.replace_window.replace_dialog_window.update()
        if (self.replace_window.command is 'skip'):
            return False
        elif (self.replace_window.command is 'replace'):
            return True
        elif (self.replace_window.command is 'skip_all'):
            self.skip_all = True
            return False
        elif (self.replace_window.command is 'replace_all'):
            self.replace_all = True
            return True


    def create_progress_window(self):
        self.console_window = Filedialogs.console_dialog(self, self.console_icon, self.reset_replace)

    def progress(self, file_name, status):
        # If it is a progress
        if ('%' in status):
            self.console_window.progress(status)
            return
        if (status == 'newline'):
            self.console_window.insert('')
            return
        # Print to console
        self.console_window.insert(status + ': ' + file_name)
    """

    def disable_toolbar(self, event=None):
        # Disable all buttons
        self.canvas.grab_set()
        # Disable mouse action
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Double-Button-1>")
        self.canvas.unbind("<Control-Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Motion>")

    def enable_toolbar(self, event=None):
        # Enable all buttons
        self.canvas.grab_release()
        # Enable mouse action
        self.canvas.bind("<Button-1>", self.mouse_select)
        self.canvas.bind("<Double-Button-1>", self.change_dir)
        self.canvas.bind("<Control-Button-1>", self.ctrl_select)
        self.canvas.bind("<B1-Motion>", self.drag_select)
        self.canvas.bind("<Motion>", self.update_status_and_mouse)


    def start_wait(self, event=None):
        if (self.change_status is False): return
        if (self.continue_wait is True):
            self.continue_wait = False
            return
        self.disable_toolbar()
        self.wait_anim = True
        self.wait_frame_index = 1
        self.after(100, self.do_wait)

    def cont_wait(self, event=None):
        self.continue_wait = True

    def do_wait(self, event=None):
        if (self.wait_anim is False): return
        # make sure frame index is not above 4
        if (self.wait_frame_index == 4):
            self.wait_frame_index = 0
        # clear and draw the correct frame
        self.canvas.delete('all')
        self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2,
                                 image=self.wait_frames[self.wait_frame_index])
        # update frame index
        self.wait_frame_index += 1
        # call the do wait function after some time to update the animation
        if (self.wait_frame_index == 1):
            self.after(400, self.do_wait)
        else:
            self.after(100, self.do_wait)

    def end_wait(self, event=None):
        self.wait_anim = False
        self.enable_toolbar()

    def problem(self, event=None):
        self.end_wait()
        self.canvas.delete('all')
        self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.problem_icon)