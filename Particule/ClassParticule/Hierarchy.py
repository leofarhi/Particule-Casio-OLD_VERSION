from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
import tkinter as tk
import time
from ClassSystem.EditorWindow import EditorWindow
from ClassParticule.GameObject import GameObject
from ClassParticule.Vector2 import Vector2

class Hierarchy(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self,RootWindow,Resize=True,ScrollbarShow=False)

        self.allGameObjectOnScene={}
        self.ItemSelected=None
        self.moveitem = tkinter.StringVar()
        self.vs = ttk.Scrollbar(self,orient="vertical")
        self.t = ttk.Treeview(self, columns=("chemin", "type"), selectmode="browse", show="tree",
                              displaycolumns=(),
                              yscrollcommand=lambda deb, fin: self.setscrl(self.vs, deb, fin))
        self.vs["command"] = self.t.yview
        self.t.heading("chemin", text="chemin")
        #self.t.insert("", 0, "Scene1", text=self.Particule.Scene.nameScene, values=(None, "dir"))
        for scene in self.Particule.Scene.scenes:
            self.t.insert("", "end", scene, text=(scene.split("/")[-1]).split(".")[0], values=(scene, "dir"))
        """self.t.insert("", 0, "dir1", text="GameObject 1", values=("d1", "dir"))
        self.t.insert("dir1", "end", "dir 1", text="GameObject 3", values=("f1", "file"))
        ID = self.t.insert("", "end", "dir2", text="GameObject 2", values=("d1", "dir"))
        self.t.insert("dir2", "end", text="GameObject 4", values=("d2", "dir"))
        self.t.insert(ID, "end", text="GameObject 5", values=("d3", "dir"))
        self.t.insert(ID, "end", text="GameObject 6", values=("f1", "file"))
        self.t.insert(ID, "end", text="GameObject 7", values=("f1", "file"))
        self.t.insert(ID, "end", text="GameObject 8", values=("f1", "file"))"""
        self.t.pack(side="left",fill=BOTH, expand=True)#.grid(column=0, row=0, sticky='EWNS')
        self.vs.pack(side = RIGHT, fill="y")#.grid(column=1, row=0, sticky='EWNS')
        self.save_cursor = self.t['cursor'] or ""

        self.mitem = tkinter.Toplevel(self)
        self.mitem.overrideredirect(1)
        self.mitem.config(bg="white")
        self.mitem.withdraw()

        self.t.bind("<ButtonRelease-1>", self.mouserelease)
        self.t.bind("<B1-Motion>", self.movemouse)

        self.t.tag_configure('Active', foreground='black')
        self.t.tag_configure('Desactive', foreground='gray')

        """initialise dialog"""
        # Button-3 is right click on windows
        self.t.bind("<Button-3>", self.popup)
        self.contextMenu = Menu(self.Particule.Mafenetre,tearoff=False)
        self.contextMenu.add_command(label="Copy")
        self.contextMenu.add_command(label="Past")
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Rename")
        self.contextMenu.add_command(label="Duplicate")
        self.contextMenu.add_command(label="Delete",command = self.deleteObject)
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Select Children")
        self.contextMenu.add_command(label="Select Prefab Root")
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Create Empty")
        self.contextMenu.add_command(label="2D Object")
        self.contextMenu.add_command(label="Effects")
        #self.contextMenu.add_command(label="Light")
        self.contextMenu.add_command(label="UI")
        self.contextMenu.add_command(label="Camera")

    def popup(self, event):
        """action in event of button 3 on tree view"""
        # select row under mouse
        iid = self.t.identify_row(event.y)
        if iid:
            # mouse pointer over item
            self.t.selection_set(iid)
            self.contextMenu.post(event.x_root, event.y_root)
        else:
            # mouse pointer not over item
            # occurs when items do not fill frame
            # no action required
            pass
    def deleteObject(self,*args):
        temp = self.t.focus()
        if self.t.parent(temp) == "":
            return
        self.DestroyGameObject(temp)
    def DestroyGameObject(self,temp):
        dico = self.GetDictOfChild(temp,{})
        #del self.allGameObjectOnScene[temp['values'][0]]
        for index,i in dico.items():
            try:
                self.allGameObjectOnScene[index].Destroy()
                del self.allGameObjectOnScene[index]
            except:
                pass
        self.t.delete(temp)


    def CreateObject(self, root=None, name=None, gameObject=None):
        if root == None:
            root = self.t.get_children("")[0]
        if gameObject == None:
            count = 0
            for _, i in self.allGameObjectOnScene.items():
                if "GameObject" in i.name:
                    count+=1
            nb = ""
            if count>0:
                nb=" ("+str(count)+")"
            gameObject = GameObject(self.Particule,"GameObject"+nb,self.t.set(self.t.get_children("")[0], "chemin"))
        if name == None:
            name = gameObject.name
        if gameObject.activeSelf:
            tag = 'Active'
        else :
            tag = 'Desactive'
        self.allGameObjectOnScene.update({gameObject.ID:gameObject})
        NewT = self.t.insert(root, "end",str(gameObject.ID) , text=name, values=(gameObject.ID, "dir"), tags=(tag))
        self.t.see(NewT)
        self.t.update()
        return gameObject
    def setscrl(self, s, d, f):
        d = float(d)
        f = float(f)
        if d <= 0 and f >= 1:
            pass#s.grid_remove()
        else:
            s.set(d, f)
            #s.grid()

    def movemouse(self, event):
        self.t = event.widget
        n = self.t.selection()
        self.moveitem.set(self.t.focus())
        x = event.x
        y = event.y
        self.mitem.geometry("%dx%d+%d+%d" % (20, 10, x, y + 90))
        self.mitem.deiconify()
        self.t['cursor'] = "hand2"
        # DragAndDropSys
        self.Particule.DragAndDropSys.Drag()

    def foundChild(self, parent, dest):
        reponse = False
        for e in self.t.get_children(parent):
            if e == dest:
                return True
            else:
                reponse = reponse or self.foundChild(e, dest)
        return reponse
    def GetDictOfChild(self,parent,dico):
        dico.update({self.t.set(parent, "chemin"):(self.t.parent(parent),self.t.set(parent, "type"))})
        for e in self.t.get_children(parent):
            dico = self.GetDictOfChild(e,dico)
        return dico
    def SetItemSelect(self):
        # print(self.t.get_children("")[0])
        try:
            tempI = self.t.item(self.t.focus())['values'][0]
            if self.t.parent(tempI) == "":
                tempI = None
                return
            if (tempI == "None"):
                tempI = None
            else:
                tempI = tempI
                self.ItemSelected = self.allGameObjectOnScene[tempI]
                self.Particule.DragAndDropSys.Drop({"Object":self.ItemSelected,"Window":"Hierarchy","Type":"GameObject"})
            self.Particule.Inspector.UpdateItemSelected()
        except:
            return
    def mouserelease(self, event):
        self.mitem.withdraw()
        self.t = event.widget
        self.t['cursor'] = self.save_cursor
        src = self.moveitem.get()
        self.Particule.ScreenOrganization.ChangeInspector("Inspector")
        self.SetItemSelect()
        # DragAndDropSys
        self.Particule.DragAndDropSys.Drop()

        if src and self.t.identify_region(event.x, event.y) == "tree":
            dest = self.t.identify_row(event.y)
            if self.foundChild(src, dest):
                self.moveitem.set("")
                return
            if self.t.set(dest, "type") == "file":
                dest = self.t.parent(dest)
            if self.t.set(src, "type") == "file":
                if self.t.parent(src) == dest:
                    self.moveitem.set("")
                    return
            else:
                if src == dest:
                    self.moveitem.set("")
                    return
            if self.t.set(src, "type") == "dir":
                src_chemin=self.t.set(src, "chemin")
                src_text=self.t.item(src, "text")
                dico = self.GetDictOfChild(src,{})
                dico.update({self.t.set(src, "chemin"):(self.t.set(dest, "chemin"),self.t.set(src, "type"))})
                self.t.delete(src)

                for index,i in dico.items():
                    me = self.allGameObjectOnScene[index]
                    if me.transform.parent != None:
                        me.transform.parent.childs.remove(me.transform)
                    if self.t.parent(i[0]) == "":#i[0] == None or i[0] == "None":
                        #i=(self.t.get_children("")[0],i[1])
                        me.transform.parent = None
                        me.scene = i[0]
                    else:
                        newVect = Vector2().set(me.transform.position.get())
                        me.transform.parent = self.allGameObjectOnScene[i[0]].transform
                        me.transform.UpdateOnGUI()
                        me.transform.position.set(newVect.get())
                        me.transform.parent.childs.append(me.transform)
                    NewT = self.t.insert(i[0], "end",index, text=me.name,
                                  values=[index, i[1]])
                    self.t.see(NewT)
                    self.t.update()
                """ID = self.t.insert(dest, "end", text=src_text,
                                   values=[src_chemin, "dir"])

                for e in self.t.get_children(src):
                    txt = self.t.item(e, "text")
                    chm = self.t.set(e, "chemin")
                    tp = self.t.set(e, "type")
                    self.t.delete(e)
                    # t.update()
                    # pour simuler le mouvement

                    # time.sleep(0.3)
                    elem = self.t.insert(ID, "end", chm, text=txt, values=[chm, tp])
                    self.t.see(elem)
                    self.t.update()

                self.t.delete(src)"""

            else:
                txt = self.t.item(src, "text")
                chm = self.t.set(src, "chemin")
                self.t.delete(src)
                # time.sleep(0.3)
                ID = self.t.insert(dest, "end", chm, text=txt, values=[chm, "file"])
                self.t.see(ID)
                self.t.update()
        self.moveitem.set("")

