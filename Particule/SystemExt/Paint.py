#=======================================================================
#........,,,,,,,,;;;;;;;;:::::::::::!!!!!!!!! >> PAINT << !!!!!!!!::::::::;;;;;;;;,,,,,,,,..........
#=======================================================================
__author__ = "Hicham S'hih"
# Python Version 3.5.2

##  EMAIL >>>>> shih.hicham@cesim.as.ma

############################# MODULES ############################
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
from tkinter import *
from random import choice
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename, askopenfilename
import tkinter.font
from ctypes import windll 
from PIL import ImageGrab, Image
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =os.getcwd()+"/gs/gs9.53.3/bin/gswin32c.exe"
import os
import TransformImage as Timg



class Paint :  #CLASS PAINT
    
    #===============================================
    #************************* INITIALISATIONS **********************
    #===============================================

    def __init__(self, master):
        self.root = master
        self.Wintaille=6
        self.Largeur = 127*self.Wintaille # Largeur de canvas par defaut est 500 px
        self.Hauteur = 63*self.Wintaille # Hauteur de canvas par defaut est 500 px
        # ==================== frame ================
        self.frmotl = Frame (self.root,width = 200, height = 100) # frame Outils (penceaux, couleur, formes...)
        self.frmotl.pack(side = TOP)
        self.frmdim = Frame (self.root) # frame Scale les barre de dimenssion
        self.frmdim.pack(side = TOP)
        self.frmstatue = Frame(self.root, width = 700, height = 20) # frame de Statues
        self.frmstatue.pack(side = BOTTOM, anchor = "nw")
        self.frmcnv = Frame (self.root, width = 129*self.Wintaille, height = 65*self.Wintaille) # frame canvas pour dissiner
        self.frmcnv.pack(side = LEFT, anchor = NW)
        self.frmaide = Frame (self.root)
        self.frmaide.pack(anchor = E)
        # ================== initialisation Setup ================
        self.defaultclr = "black" # 1er couleur par defaut est le Noir
        self.defaultclr_2 = "white" # 2eme couleur par defaut est le blanc
        
        # ================== Preparation de la zone de dessin =================
        self.canvas = Canvas(self.frmcnv,cursor="pencil", bg='white',relief = GROOVE, width = self.Largeur, height = self.Hauteur)
        self.canvas.grid(row=0, sticky = NW)
        self.canvas.update()
        self.ConfigObjet = None
        self.size = 1
        self.filename = ""
        self.BtnClrActif = 1
        self.Menu()
        self.guid()
        self.setup()

        self.favsize(self.Wintaille)
        
    #===============================================
    #*************************** INTERFACE **************************
    #===============================================

    # ================ Creation de Menu ==============
    def Menu(self):
        self.menubar = Menu(self.root) # la barre Menu
        self.root.config(menu=self.menubar)
        self.menu = Menu(self.menubar, tearoff=False) # 1er Menu pour file
        self.menu1 = Menu(self.menubar, tearoff=False) # 2eme Menu pour affichager
        # les images de labels
        self.Penceauximg, self.about, self.new, self.open, self.save, self.saveas, self.ext =PhotoImage(file = "lib/icone/Penceauximg.png"), PhotoImage(file = "lib/icone/about.png"), PhotoImage(file = "lib/icone/new.png"), PhotoImage(file = "lib/icone/open.png"), PhotoImage(file = "lib/icone/save.png"), PhotoImage(file = "lib/icone/saveas.png"), PhotoImage(file = "lib/icone/ext.png")
        # menu file
        self.menubar.add_cascade(label="File", menu=self.menu)
        self.menu.add_command(label="Nouveau", image = self.new, compound = LEFT, command=self.Nouveau)
        self.menu.add_command(label="Ouvrir", image = self.open, compound = LEFT, command=self.Ouvrir)
        self.menu.add_command(label="Enregistrer",image = self.save, compound = LEFT, command=self.Enregistrer)
        self.menu.add_command(label="Enregistrer_Sous",image = self.saveas, compound = LEFT, command=self.Enregistrer_Sous)
        self.menu.add_command(label="A Propos",image = self.about, compound = LEFT, command=self.About)
        self.menu.add_command(label="Quiter",image = self.ext, compound = LEFT, command=self.Exit)
        # menu affichage
        #self.menubar.add_cascade(label="Affichage", menu=self.menu1)
        self.menu1.add_command(label="Redimonssioner", command = self.get_x_y_canvas)
        self.menu1.add_command(label="Plain Ecran", command = self.PE)
        self.menu1.add_command(label="Ecran Simple", command = self.ES)

    # la Creation des buttons
    def guid (self):
        # les images pour les buttons
        self.imgclraide, self.dimcnvimg, self.lessauv, self.taillesaide = PhotoImage(file = "lib/icone/imgclraide.png"),PhotoImage(file = "lib/icone/dimcnvimg.png"),PhotoImage(file = "lib/icone/lessauv.png"),PhotoImage(file = "lib/icone/taillesaide.png")
        self.carre,self.circle,self.pen,self.s1,self.s2,self.s3,self.s4, self.gomme = PhotoImage(file = "lib/icone/carre.png"),PhotoImage(file = "lib/icone/cercle.png"),PhotoImage(file = "lib/icone/crayon.png"),PhotoImage(file = "lib/icone/s1.gif"),PhotoImage(file = "lib/icone/s2.gif"),PhotoImage(file = "lib/icone/s3.gif"),PhotoImage(file = "lib/icone/s4.gif"),PhotoImage(file = "lib/icone/gomme.png")
        self.rempcnt, self.modifierclr, self.iline,self.imnone, self.Atext, self.aerographe = PhotoImage(file="lib/icone/rempcnt.png"), PhotoImage(file="lib/icone/Modifierclr.png") , PhotoImage(file="lib/icone/line.png"),PhotoImage(file="lib/icone/none.png") ,PhotoImage(file="lib/icone/Atext.png"), PhotoImage(file="lib/icone/aérographe.png")
        self.triangle, self.remplir,self.contour, self.penhor, self.penver, self.past, self.detct, self.rempl =PhotoImage(file = "lib/icone/triangle.png") ,PhotoImage(file = "lib/icone/remplir.png"),PhotoImage(file = "lib/icone/contour.png"),PhotoImage(file = "lib/icone/penhor.png"),PhotoImage(file = "lib/icone/penver.png"),PhotoImage(file = "lib/icone/pastel.png"),PhotoImage(file = "lib/icone/detecteur.png"), PhotoImage(file = "lib/icone/remplisseur.png")
        # partie des Outils (5 outils > pencil > gomme > text > detecteur, selection)
        self.btnpen = ttk.Button(self.frmotl, image = self.pen, width = 25, command=self.pencil); self.btnpen.grid(row = 0, column = 2)
        self.btngomme = ttk.Button(self.frmotl, image = self.gomme, width = 25, command=self.actgomme); self.btngomme.grid(row = 0, column = 3)
        #self.btnatxt = ttk.Button(self.frmotl, image = self.Atext, width = 25, command=self.actatxt); self.btnatxt.grid(row = 0, column = 4)
        #self.btnone = ttk.Button(self.frmotl, image = self.imnone, width = 25, command=self.none); self.btnone.grid(row = 1, column = 2, columnspan = 2)
        #self.btndet = ttk.Button(self.frmotl, image = self.detct, width = 25, command = self.actdet); self.btndet.grid(row = 1, column = 3, columnspan = 2)
        self.txtstat = Label (self.frmotl, text = "Outils",width = 12).grid(row = 2, column = 2, columnspan = 3)
        """
        self.seplbl = Label(self.frmotl, text = "|\n|\n|\n|").grid(row = 0, rowspan = 3, column = 5)
        # partie des Penceaux (4 penceaux > pen-vertical > pen-horizontal > pastel > aerographe)
        self.btnaero = ttk.Button(self.frmotl, image = self.aerographe, width = 25, command=self.actaero); self.btnaero.grid(row = 0 , column = 6)
        self.btnpast = ttk.Button(self.frmotl, image = self.past, width = 25, command = self.actpast); self.btnpast.grid(row = 0 , column = 7)
        self.btnver = ttk.Button(self.frmotl, image = self.penver, width = 25, command = self.actpenv); self.btnver.grid(row = 1 , column = 6)
        self.btnhor = ttk.Button(self.frmotl, image = self.penhor, width = 25, command = self.actpenh); self.btnhor.grid(row = 1 , column = 7)
        self.txtstat = Label (self.frmotl, text = "Penceaux",width = 12).grid(row = 2, column = 6, columnspan = 2)
        self.seplbl = Label(self.frmotl, text = "|\n|\n|\n|").grid(row = 0, rowspan = 3, column = 8)
        # partie des Formes (4 formes > line > oval > rectangle > triangle-rect)
        self.btnline = ttk.Button(self.frmotl, image = self.iline,width = 25, command=self.actline); self.btnline.grid(row = 0, column = 9)
        self.btncircle = ttk.Button(self.frmotl, image = self.circle, width = 25, command=self.actcircle); self.btncircle.grid(row = 0, column = 10)
        self.btncarre = ttk.Button(self.frmotl, image = self.carre, width = 25, command=self.actcarre); self.btncarre.grid(row = 1, column = 9)
        self.btntrian = ttk.Button (self.frmotl, image = self.triangle, width = 25, command = self.acttriangle); self.btntrian.grid(row = 1, column = 10)
        self.btnremp = ttk.Button (self.frmotl, image = self.remplir,width = 65, state = DISABLED, command = self.rempliser); self.btnremp.grid(row = 0, column = 11, columnspan = 2)
        self.btncntr = ttk.Button (self.frmotl, image = self.contour,width = 65, state = DISABLED, command = self.contObjet); self.btncntr.grid(row = 1, column = 11, columnspan = 2)
        self.txtstat = Label (self.frmotl, text = "Formes",width = 12).grid(row = 2, column = 9, columnspan = 4)
        
        self.seplbl = Label(self.frmotl, text = "|\n|\n|\n|").grid(row = 0, rowspan = 3, column = 13)
        # partie des Tailles ( 4 tailles > size 1 > 2 > 3 > 4)
        self.btns1 = ttk.Button(self.frmotl, image = self.s1,command = lambda x=1 : self.favsize(x)); self.btns1.grid(row = 0, column = 14)
        self.btns2 = ttk.Button(self.frmotl, image = self.s2,command = lambda x=2 : self.favsize(x)); self.btns2.grid(row = 1, column = 14)
        self.btns3 = ttk.Button(self.frmotl, image = self.s3,command = lambda x=3 : self.favsize(x)); self.btns3.grid(row = 0, column = 15)
        self.btns4 = ttk.Button(self.frmotl, image = self.s4,command = lambda x=4 : self.favsize(x)); self.btns4.grid(row = 1, column = 15)
        self.txtstat = Label (self.frmotl, text = "Tailles",width = 12).grid(row = 2, column = 14, columnspan = 2)
        """

        """
        self.seplbl = Label(self.frmotl, text = "|\n|\n|\n|").grid(row = 0, rowspan = 3, column = 16)
        # partie couleurs ( 8 couleur par defaut et button askcolot + 2 buttons pour la couleur choisi)
        self.clr = Button (self.frmotl, bg = self.defaultclr,width = 3, command = lambda pos = 1 : self.ActiveBtnClr(pos)); self.clr.grid(row=0, column = 17)
        self.txtstat = Label (self.frmotl, text = "  ").grid(row = 1, column = 17, columnspan = 2)
        self.clr_2 = Button (self.frmotl, bg = self.defaultclr_2,width = 3, command = lambda pos = 2 : self.ActiveBtnClr(pos)); self.clr_2.grid(row=1, column = 17)
        #self.black = Button (self.frmotl, bg = "black",  command = lambda x = "black" : self.changerclr(x)); self.black.grid(row=0, column = 19)
        """
        
        """
        self.brown = Button (self.frmotl, bg = "brown",  command = lambda x = "brown" : self.changerclr(x)); self.brown.grid(row=0, column = 20)
        self.orange = Button (self.frmotl, bg = "orange",  command = lambda x = "orange" : self.changerclr(x)); self.orange.grid(row=0, column = 21)
        self.red = Button (self.frmotl, bg = "red",  command = lambda x = "red" : self.changerclr(x)); self.red.grid(row=0, column = 22)
        self.yellow = Button (self.frmotl, bg = "yellow", command = lambda x = "yellow" : self.changerclr(x)); self.yellow.grid(row=0, column = 23)
        """
        #self.white = Button (self.frmotl, bg = "white",  command = lambda x = "white" : self.changerclr(x)); self.white.grid(row=1, column = 19)
        """
        self.green = Button (self.frmotl, bg = "green",  command = lambda x = "green" : self.changerclr(x)); self.green.grid(row=1, column = 20)
        self.blue = Button (self.frmotl, bg = "blue", command = lambda x = "blue" : self.changerclr(x)); self.blue.grid(row=1, column = 21)
        self.cyan = Button (self.frmotl, bg = "cyan",  command = lambda x = "cyan" : self.changerclr(x)); self.cyan.grid(row=1, column = 22)
        self.pink = Button (self.frmotl, bg = "pink", command = lambda x = "pink" : self.changerclr(x)); self.pink.grid(row=1, column = 23)
        self.favclr = ttk.Button(self.frmotl, text = "Couleur", image = self.modifierclr, width = 10, compound="left", command = self.choose_color); self.favclr.grid(row = 0, rowspan = 2 , column = 24, columnspan = 2)
        self.txtstat = Label (self.frmotl, text = "Couleur",width = 20).grid(row = 2, column = 17, columnspan = 8)
        """

        
        # partie des statue une de l'intoduction et l'autre pour des info à l'utilisateur (size, position, clrs ...)
        self.lblstatue = Label(self.frmstatue, text= "( x :     y :  ) \t\t Pencil \t\t clr1 : Black \t\t clr2 : white \t\t size :1", fg = "cornsilk", bg='orange',width = self.Largeur, anchor = W, font = ("arial", 10, "bold"), relief = SUNKEN); self.lblstatue.pack()
        #self.lblstatue2 = Label(self.frmstatue, text= "hello world", fg = "black", bg='light blue',width = self.Largeur, anchor = W, font = ("arial", 10, "bold"), relief = SUNKEN); self.lblstatue2.pack()
        # partie pour redimenssioner le canvas avec Scale
        #self.lbldim = Label (self.frmdim, text = "Dimenssioner canvas", fg = "red"); self.lbldim.pack(side = LEFT)
        #self.scaledim = Scale(self.frmdim, orient = HORIZONTAL, length = 250,from_ = 200, to = 500, showvalue = 0)
        #self.scaledim.pack()
        #self.scaledim.bind("<B1-Motion>", self.gettt)
        """

        self.lblerror = Label(self.frmaide, text = "Poser Votre Question Je Peut T'aider :*").pack()
        self.optionList = ("Avez Vous Besion d'aide ?", "Comment Ecrir un text",
                                 "Comment Selectionner et deplacer ?" , "Comment detecter la couleur ?",
                                 "Quel est la différance\nentre les penceaux ?", "Comment changer la couleur d'un objet ?",
                                 "Pourqoui les buttons remplir et \ncontour sont bloquées?",
                                 "Quel est les tailles disponible ?", "Comment choisi une autre couleur?",
                                 "Comment sauvgarder ?", "Comment redimonsioner l'image?",
                                 "Quel sont les extension disponibles?", "Pourquoi je peuve pas ouvrie une image?")
        self.v = StringVar()
        self.Myaide = Entry(self.frmaide, textvariable = self.v, width = 35)
        self.v.set("Quel est Votre Question ...")
        self.Myaide.pack()
        self.btnaide = ttk.Button(self.frmaide, text = "Chercher"); self.btnaide.pack()
        self.Myaide.bind("<Button-1>", self.clearzone) 
        self.btnaide.bind("<Button-1>", self.getquest)
        self.setaide  = Label (self.frmaide, text = ""); self.setaide.pack(anchor = E)
        """
    def clearzone (self, event):
        self.v.set ("")
        self.imgaide = None
        self.setaide.config(text = "")
    def getquest(self, event):
        a = self.v.get()
        b = 0
        if len(a) >= 3:            
            for option in self.optionList :
                if a in option : 
                    self.getrep(option)
                    if self.imgaide != None:
                        self.setaide.config(text = self.setrep, image = self.imgaide, compound = TOP)
                    else : self.setaide.config(text = self.setrep)
                    b += 1
            if b == 0:
                self.setaide.config(text = "Désolé > il y a aucun resulta pour\nvotre saisie : {}".format(a))
            else : b=0
    def getrep(self, option):
        if option == self.optionList[1] : self.imgaide = self.Atext;self.setrep = self.optionList[1] + " :\n\n\nAppuyer sur le Button 'A' qui se \ntrouve dans Outils après\nfaire clicker dans la position\noù tu veux ecrire dans la feuille\nécrire votre text et appuie sur 'Write'"
        elif option == self.optionList[2] : self.imgaide = self.imnone;self.setrep = self.optionList[2] + " :\n\n\nPour selectioner et deplacer \nfaire un glissement entre\ndeux points\nPS : il faut que tu fait le\nglissement de haut vers\nle bas et de gauche\nvers droite\n>>après faire click à l'interieur\nde la selection et deplacer l'image\n> - pour une autre selection click\na l'exterieur de la selection"
        elif option == self.optionList[3] : self.imgaide = self.detct;self.setrep = self.optionList[3] + " :\n\n\ncliquer dans n'import position\net la couleur detecter s'envoie\nvers le boutton de couleur\n1er Button"
        elif option == self.optionList[4] : self.imgaide = self.Penceauximg;self.setrep = self.optionList[4] + " :\n\n\n Aerographe : est un pistolet à peinture\nminiature dissiner Plusieur points ou ligne\nPastel : dissiner plusieur points\ndans une intervalle petite\n pencil-vertical ou horizontal: \nsont des crayons de calligraphie"
        elif option == self.optionList[5] : self.imgaide = self.remplir; self.setrep = self.optionList[5] + " :\n\n\naprès de dissiner votre forme\nchoisie une couleur et\nAppuie sur le button remplir"
        elif option == self.optionList[6] : self.imgaide = self.rempcnt; self.setrep = self.optionList[6] + " :\n\n\nLes Buttons sont bloquée quand\nil y a pas d'objet a configurer\nles button sont active quand\nun button de formes est\nactiver"
        elif option == self.optionList[7] : self.imgaide = self.taillesaide; self.setrep = self.optionList[7] + " :\n\n\nLes Tailles disponible sont\n4 Tailles une petite et l'autre\nplus grand que la premier...ect"
        elif option == self.optionList[8] : self.imgaide = self.imgclraide; self.setrep = self.optionList[8] + " :\n\n\nAppuie sur le Button couleur\naprès choisi la couleur\npreferent appuie sur OK et votre\ncouleur ce trouve dans le Button\n1er de clr" 
        elif option == self.optionList[9] : self.imgaide = self.lessauv; self.setrep = self.optionList[9] + " :\n\n\nPour sauvgarder Appuie sur\nfile au menu après Enregister\nsi votre traviller et déja enregistrer\n sinon appuie sur enregistrer-sous\ntitré votre image et choisie\nl'extensio par defaut et .PNG\ncliquée a la fin sur enregistrer\n s'il a bien enregister le titre de \n programme vas changer par le nom\nentrer par vous"
        elif option == self.optionList[10] : self.imgaide = self.dimcnvimg ; self.setrep = self.optionList[10] + " :\n\n\nPour redimenssioner votre image glisser\nla barre au-dessue la feuille ou cliquée\nsur affichage après clicque sur\nredimenssioner entrer les valeur\nde la hauteur et la largeur\naprès appuie sur redimenssioner\nPS : il faut que la largeur et\nla hauteur entre 200 px et 500 px" 
        elif option == self.optionList[11] : self.setrep = self.optionList[10] + " :\n\n\nLes extension disponible sont .png et .gif\n PS : faire attention dans la sauvgarde de\ntravaill pour l'extension!!"
        elif option == self.optionList[12] : self.setrep = self.optionList[10] + " :\n\n\nPour Ouvrir une image il faut que\nl'image ne depasse pas 500 px\net d'étre pas moins de 200px\nPS : l'image ne s'affiche\npas s'il l'extension de\nl'image est different de .png ou .gif\n"

        
        
        
    # fonction pour Scale et de la configuration des dimonssions de canvas   
    def gettt(self, event):
        self.Largeur, self.Hauteur = self.scaledim.get(), self.scaledim.get()
        self.canvas.config(width = self.scaledim.get(), height = self.scaledim.get())


    # fonction Setup pour la creation des variables par defauts
    def setup(self):
        self.old_x, self.old_y = None, None # sont les coordonner des 1er x,y s'il y a un glissement dans le canvas
        self.last_x, self.last_y = None, None # sont les coord des dernier x,y s'il ya un glissement dans le canvas
        self.old_btn = self.btnpen # c'est le Button activer dans l'execution "Pencil"
        self.Mytxt = "" # variable vide >>  pour le mode text dans le canvas 
        self.Ecran_mode = "Simple" # dans l'execution la fenetre s'ouver on mode Simple >l'autre mode est Plain écran
        self.moveselect = 0 # variable pour detect s'il y a une selction dans le canvas ou pas
        self.mode = "Pencil" # le mode defaut dans l'execution
        self.esp_st = 0 # Pour lbl Statue ajouter des espaces pour un mouvement de text vers la droite
        self.Myclrst = ["blue","orange"] # les couleur de text de statue introduction
        self.canvas.bind('<Button-1>', self.Draw_point)#self.atext) # S'il y a une click dans le canvas et le mode Text activer l'utlisateur peuve ecrit dans le canvas
        self.canvas.bind('<B1-Motion>', self.Draw) # quand il ya un click-mouvement dans le canvas


        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomer)
           
        self.canvas.bind('<ButtonRelease-1>', self.reset) # quand l'utlis laisse la click les variable sont returner par defaut à la valeur d'execution
        self.root.after(100, self.intro) # pour un mouvement de text

    # fonction qui present le projet par une statue movable :p
    def intro (self):
        return
        if self.esp_st >= 180 :
            self.txtstatue = " "*(self.esp_st-400) +  "             <<CESIM>>             Paint             <<CESIM>>             Hicham-S'hih             <<CESIM>>             2éme-Année             <<CESIM>>             Python-V3.5.2              <<CESIM>>            ..MH..                                         "
            self.lblstatue2.config(text = self.txtstatue[-self.esp_st+179:], fg = choice(self.Myclrst), bg = self.defaultclr)
            if self.esp_st-180 == len(self.txtstatue)-1:
                self.esp_st=0
            self.esp_st += 1
        else:
            self.txtstatue = " "*self.esp_st +  "             <<CESIM>>             Paint             <<CESIM>>             Hicham-S'hih             <<CESIM>>             2éme-Année             <<CESIM>>             Python-V3.5.2              <<CESIM>>            ..MH..                                        " 
            self.lblstatue2.config(text = self.txtstatue, fg = choice(self.Myclrst), bg = self.defaultclr)
            self.esp_st += 1
        self.root.after(60, self.intro)

    # fonction dans la click sur le button exit (ask user to save work else kill apps)
    def Exit (self):
        if messagebox.askokcancel("Quittez Paint ?", "Etes-vous sûr de vouloir quitter Paint?\n\nEn cliquant sur 'OK' Paint se fermera"):
            if self.filename == "":
                if messagebox.askokcancel("Sauvgarder !", "Voulez-vous sauvgarder votre Travail ?"):
                    self.Enregistrer()
                self.root.destroy()

    def PE (self): # plain Ecran
        self.Ecran_mode = "Plain"
        self.root.attributes('-fullscreen',True)

    def ES (self): # Ecran Simple
        self.Ecran_mode = "Simple"
        self.root.attributes('-fullscreen',False)

    def Nouveau (self): # supprimer tout ce qu'il ya dans le canvas
        self.canvas.delete("all")

    def Ouvrir (self, filename = None): # Ouvrir une image dans le canvas
        if filename is not None : self.opename = filename
        else:
            #ftypes = [ ('PNG', '.png'), ('GIF', '.gif')]
            self.opename = askopenfilename( title='Open image',#filetypes=ftypes,
                                           defaultextension='.png')
            
        #self.im = Image.open(self.opename).convert("RGB")
        #self.im.save("TempImage.png","png")
        #self.image_open = PhotoImage(file = "TempImage.png")#Image.open(self.opename).convert("RGB"))#file = self.opename)
        Lines=Timg.create_line(Timg.arraylst(Timg.ImageConvert(self.opename)))
        Wintaille=self.Wintaille
        x,y=0,1
        for i in Lines:
            self.canvas.create_line((i[1]*Wintaille)-(x*Wintaille),(i[0]*Wintaille)+(y*Wintaille), ((i[1]+i[2])*Wintaille)-(x*Wintaille),(i[0]*Wintaille)+(y*Wintaille), fill="black", width=Wintaille)
        """
        self.x_img, self.y_img = self.im.size
        if True:#200 <= self.x_img <= 500 and 200 <= self.y_img <= 500 :
            self.getoffset()
            self.canvas.create_image (self.x_offset+250,self.y_offset+250, image = self.image_open)
            if self.x_img > self.Largeur or self.y_img > self.Hauteur:
                self.canvas.config (width = self.x_img, height = self.y_img)
        else :
            messagebox.showerror("Erreur d'ouverture", "La Taille de Votre image doit étre entre 300 et 600")
            return
        """
    def save_as_png(self,canvas,fileName):
        
        # save postscipt image 
        canvas.postscript(file = "tempImg" + '.eps') 
        # use PIL to convert to PNG 
        img = Image.open("tempImg" + '.eps')#.convert('RGB')
        img.save(fileName,'png')# + '.png', 'png')
        #os.remove("tempImg" + '.eps')

    #windows zoom
    def zoomer(self,event):
           return
           if (event.delta > 0):
               self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
           elif (event.delta < 0):
               self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
           self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #linux zoom
    def zoomerP(self,event):
           return
           self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
           self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    def zoomerM(self,event):
           return
           self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
           self.canvas.configure(scrollregion = self.canvas.bbox("all"))
        
    def Enregistrer (self): # enregister le travail ça marche si il ya déja une sauvgarde sinn il appel la fonction enregister-sous
        if self.filename == "" :
            self.Enregistrer_Sous()
            return
        self.getoffset()
        self.canvas.update()
        self.save_as_png(self.canvas,self.filename)
        #ImageGrab.grab((self.x_offset+10, self.y_offset+155, self.Largeur+self.x_offset+10, self.Hauteur+self.y_offset+155)).save(self.filename)
        
    def Enregistrer_Sous (self, filename = None): #enregister le travail ou faire un autre enregistrement
        self.getoffset()
        
        if filename is not None: self.filename = filename
        else :
            ftypes = [('PNG', '.png'), ('GIF', '.gif')]
            self.filename = asksaveasfilename(filetypes=ftypes, title='Save image as',
                                     defaultextension='.png')
        while self.filename == "" :
            if messagebox.askokcancel("Erreur d'enregistrement", "Vous n'avez pas saisie un titre pour l'image"):
                self.filename = asksaveasfilename(filetypes=ftypes, title='Save image as',
                               defaultextension='.png')
            else : return
        self.canvas.update()
        self.save_as_png(self.canvas,self.filename)
        #ImageGrab.grab((self.x_offset+10, self.y_offset+155, self.Largeur + self.x_offset+10, self.Hauteur+self.y_offset+155)).save(self.filename)
        self.titlename = self.filename.split("/")
        self.root.title(self.titlename[-1]+" - Paint")
           
    def getoffset(self):# pour les coord de la fenetre x,y
        self.root.update()
        self.x_offset, self.y_offset = self.root.winfo_x(), self.root.winfo_y()
    
    def About (self): # A propos >> des informations a propos de moi
        self.propos = Toplevel(); self.propos.title("A Propos")
        self.prps = "\t\tPaint -- 2016/2017\t\t\n -- Créer par Hicham S'hih -- \n -- Organiser par Naoum -- \n -- Projet Fin 1er Semestre -- \n -- 2éme Année -- \n -- Ingénieurie Informatique -- \nProgrammation* \t  CESIM\t\t Python V3.5.2"
        self.mylblprp = Label(self.propos, text = self.prps).pack()
    #===============================================
    #************************** PARAMETRES *************************
    #===============================================

    def choose_color(self): # ask user to choose color 
        self.result = askcolor(self.defaultclr, title = "Couleur")
        self.changerclr (self.result[1])

    def ActiveBtnClr (self, pos) : # changer le button de couleur
        self.BtnClrActif = pos

    def changerclr (self, x): # changer la couleur
        if self.BtnClrActif == 1:
            self.defaultclr = x
            self.clr["bg"] = x
        elif self.BtnClrActif == 2:
            self.defaultclr_2 = x
            self.clr_2["bg"] = x
            
    def favsize (self, size): # pour modifier la taille pour dissiner
        self.size = size
        
    #===============================================
    #******************* ACTIVATIONS BUTTONS ********************
    #===============================================
    
    def active_button(self , btn_active, mode, cur = None, rempcont = False):
        self.old_x, self.old_y = None, None
        """
        if rempcont == True :
            self.btnremp.config(state = NORMAL)
            self.btncntr.config(state = NORMAL)
        else :
            self.ConfigObjet = None
            self.btnremp.config(state = DISABLED)
            self.btncntr.config(state = DISABLED)
        """
        self.canvas["cursor"] = cur
        """
        if self.old_btn == self.btnone:
            self.Enregistrer_Sous("cacher_/myslct.png")
            self.Ouvrir("cacher_/myslct.png")
        """
        self.old_btn = btn_active
        self.mode = mode
        self.moveselect = 0

    def none(self): # selectionner
        pass#self.active_button(self.btnone, "none", "top_left_arrow", False)

    def pencil (self):
        self.active_button(self.btnpen, "Pencil", "pencil", False)

    def actatxt (self):
        pass#self.active_button(self.btnatxt, "Text", "xterm", False)

    def actaero (self):
        pass#self.active_button(self.btnaero, "Aerographe", "spraycan", False)

    def actgomme (self):
        self.active_button(self.btngomme, "Gomme", "X_cursor", False)

    def actcircle (self):
        pass#self.active_button(self.btncircle, "Circle", "circle", True)

    def actcarre (self):
        pass#self.active_button(self.btncarre, "Carre", "dotbox", True)

    def actline (self):
        pass#self.active_button(self.btnline, "Ligne", "crosshair", False)

    def actdet (self):
        pass#self.active_button(self.btndet, "Detecteur", "hand1", False)

    def actpast (self):
        pass#self.active_button(self.btnpast, "Pastel", "target", False)

    def actpenv (self):
        pass#self.active_button(self.btnver, "Pencil Vertical", "ul_angle", False)

    def actpenh (self):
        pass#self.active_button(self.btnhor, "Pencil Horizontal", "ur_angle", False)

    def acttriangle (self):
        pass#self.active_button(self.btntrian, "Triangle-Rectangle","diamond_cross", True)

    #===============================================
    #*************************** DESSINER ****************************
    #===============================================
    def Draw_point(self, event):
        X = event.x
        Y = event.y
        event.x=int((X/self.Wintaille))*self.Wintaille
        event.y=int((Y/self.Wintaille))*self.Wintaille
        event.x+=self.Wintaille/2

        self.old_x = event.x
        self.old_y = event.y
        self.Draw(event)
    def Draw(self, event): # la fonction pour dissiner
        X = event.x
        Y = event.y
        event.x=int((X/self.Wintaille))*self.Wintaille
        event.y=int((Y/self.Wintaille))*self.Wintaille
        event.x+=self.Wintaille/2
        draw_rect=True#(self.old_x==event.x and self.old_y == event.y)

        if self.mode == "Pencil":
            if self.old_x and self.old_y: # si old_x,y sont different de None >> dissiner
                if draw_rect:
                    self.canvas.create_rectangle(self.old_x-(self.Wintaille/2), self.old_y-(self.Wintaille/2), event.x+(self.Wintaille/2)-1, event.y+(self.Wintaille/2)-1,
                          fill = self.defaultclr, outline = self.defaultclr)
                else:
                    self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width = self.size,
                          fill = self.defaultclr, capstyle = ROUND, smooth=TRUE, splinesteps = self.Wintaille)
            self.old_x = event.x # old_x prende la valeur de event.x mm pour y
            self.old_y = event.y
            # pour chaque mouvement dans le canvas il ya des configuration dans la statue
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t {} \t\t clr1 : {} \t\t clr2 : {} \t\t size :{}".format(event.x, event.y,self.mode, self.defaultclr, self.defaultclr_2, self.size))
        elif self.mode == "Aerographe":
            if self.old_x and self.old_y:
                a = list (range((self.size*-12),(self.size*12),1))
                for i in range (20): # dessiner plusieur points avec un seule event
                    x,y = choice(a), choice(a)
                    self.canvas.create_line(self.old_x+x, self.old_y+y, event.x+x, event.y+y,
                        fill = self.defaultclr, capstyle = ROUND, smooth=TRUE, splinesteps = 1)
            self.old_x = event.x
            self.old_y = event.y
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t {} \t\t clr1 : {} \t\t clr2 : {} \t\t size :{}".format(event.x, event.y,self.mode, self.defaultclr, self.defaultclr_2, self.size))
        elif self.mode == "Gomme": # la clr de la gomme est la 2eme clr choisie
            if self.old_x and self.old_y:
                if draw_rect:
                    self.canvas.create_rectangle(self.old_x-(self.Wintaille/2), self.old_y-(self.Wintaille/2), event.x+(self.Wintaille/2), event.y+(self.Wintaille/2),
                          fill = self.defaultclr_2, outline = self.defaultclr_2)
                else:
                    self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width = self.size,
                          fill = self.defaultclr_2, capstyle = ROUND, smooth=TRUE, splinesteps = 36)
            self.old_x = event.x
            self.old_y = event.y
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t {} \t\t clr1 : {} \t\t clr2 : {} \t\t size :{}".format(event.x, event.y,self.mode, self.defaultclr, self.defaultclr_2, self.size))
        elif self.mode == "Pastel":
            if self.old_x and self.old_y:
                a = list (range((self.size*-3),(self.size*3),1))
                for i in range (25):
                    x,y = choice(a), choice(a)
                    self.canvas.create_line(self.old_x+x, self.old_y+y, event.x+x, event.y+y,
                        fill = self.defaultclr, capstyle = ROUND, smooth=TRUE, splinesteps = 1)
            self.old_x = event.x
            self.old_y = event.y
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t {} \t\t clr1 : {} \t\t clr2 : {} \t\t size :{}".format(event.x, event.y,self.mode, self.defaultclr, self.defaultclr_2, self.size))
        elif self.mode == "Pencil Vertical":
            if self.old_x and self.old_y:
                for i in range (3):
                    self.canvas.create_line(self.old_x+i, self.old_y+i, event.x+i, event.y+i, width = self.size,
                          fill = self.defaultclr, capstyle = ROUND, smooth=TRUE, splinesteps = 36)
            self.old_x = event.x
            self.old_y = event.y
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t {} \t\t clr1 : {} \t\t clr2 : {} \t\t size :{}".format(event.x, event.y,self.mode, self.defaultclr, self.defaultclr_2, self.size))
        elif self.mode == "Pencil Horizontal":
            if self.old_x and self.old_y:
                for i in range (3):
                    self.canvas.create_line(self.old_x+i, self.old_y-i, event.x+i, event.y-i, width = self.size,
                          fill = self.defaultclr, capstyle = ROUND, smooth=TRUE, splinesteps = 36)
            self.old_x = event.x
            self.old_y = event.y
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t {} \t\t clr1 : {} \t\t clr2 : {} \t\t size :{}".format(event.x, event.y,self.mode, self.defaultclr, self.defaultclr_2, self.size))
        else : # si le mode est != de pencil >> aerographe >>... 
            if self.mode in ["Text","Detecteur"] : return # pour eviter l'erreur de la modification de statue
            if not (self.old_x and self.old_y) :
                self.old_x, self.old_y = event.x, event.y
            self.lblstatue.config(text = "( x : {}    y : {} ), ( x {} : {}    y {} : {} ) \t clr1 : {} \t clr2 : {} \t size :{}".format(self.old_x, self.old_y, self.mode, event.x, self.mode, event.y, self.defaultclr, self.defaultclr_2, self.size))

    def drawcircle(self): # dissiner un oval
        if self.mode == "Circle":
            try : self.ConfigObjet = self.canvas.create_oval(self.old_x, self.old_y,self.last_x,self.last_y,
                                        width = self.size, outline = self.defaultclr)
            except : return # pour eviter l'error s'il ya une click pas une mouvement

    def drawtriangle(self): 
        if self.mode == "Triangle-Rectangle":
            try :
                self.ConfigObjet = self.canvas.create_polygon(self.old_x, self.old_y, self.last_x,
                                  self.last_y, self.old_x, self.last_y, self.old_x, self.old_y,
                                  width = self.size, outline = self.defaultclr)
            except : return

    def drawline (self):
        if self.mode == "Ligne":
            try : self.canvas.create_line(self.old_x, self.old_y, self.last_x, self.last_y,
                                          width = self.size, fill = self.defaultclr)
            except : return
    def drawcarre (self):
        if self.mode == "Carre":
            try : self.ConfigObjet = self.canvas.create_rectangle(self.old_x, self.old_y, self.last_x, self.last_y,
                                    width = self.size, outline = self.defaultclr)
            except : return

    def get_x_y_canvas (self): # pour redimonsionner le canvas (prendre x,y par l'utilisateur)
        self.fd = Tk(); self.fd.title("Redimenssioner Canvas"); self.fd.resizable(True, True)#self.fd.resizable(width = False, height = False)
        self.dim_canvas_x, self.dim_canvas_y = StringVar(), StringVar() 
        self.label_x = Label(self.fd, text = "Largeur canvas : ", anchor = E).grid(row = 0, column = 0)
        self.label_y = Label(self.fd, text = "Hauteur canvas : ", anchor = E).grid(row = 1, column = 0)
        self.entry_x = Entry(self.fd, textvariable = self.dim_canvas_x); self.entry_x.grid(row = 0, column = 1)
        self.entry_y = Entry(self.fd, textvariable = self.dim_canvas_y); self.entry_y.grid(row = 1, column = 1)
        self.btn_confirmer = Button (self.fd, text = "Confirmer", command = self.redimensionner).grid(row = 2, columnspan = 2)

    def redimensionner(self, myx = None, myy = None): # redimenssioner le canvas
        try :
            x, y = int(self.entry_x.get()), int(self.entry_y.get())
        except :
            self.fd.destroy()
            return
        if ( 200 > x or x > 500 ) or ( 200 > y or y > 500 ): # si l'utilisateur a entre des valeur très grands ou petits
            messagebox.showerror ("Error", "Il faut que la largeur ou la hauteur doit être entre 300 et 600")
            self.fd.destroy()
        else : # sinon la nouvel dimmenssion de canvas
            self.Largeur, self.Hauteur = x, y
            self.canvas.config(width = x, height = y)
            self.fd.destroy()

    def atext (self, event): # pour Ecrir un text dans le canvas ou detecter la couleur
        if self.mode=="Text":
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t {} \t\t clr1 : {} \t\t clr2 : {} \t\t size :{}".format(event.x, event.y,self.mode, self.defaultclr, self.defaultclr_2, self.size))
            self.txt_x, self.txt_y = event.x, event.y
            self.wrt = StringVar()
            self.a = Tk(); self.a.resizable(True, True)#self.a.resizable(width = False, height = False) 
            self.entrer = Entry (self.a, textvariable= self.wrt); self.entrer.grid(row = 0)
            self.write = Button (self.a, text="Write!", command = self.Drawtxt); self.write.grid(row = 1)
            self.a.mainloop()
        if self.mode == "Detecteur" :
            self.lblstatue.config(text = "( x : {}    y : {} ) \t\t\t {} \t\t\t size :{}".format(event.x, event.y,self.mode, self.size))
            self.detectclr(event.x, event.y)

    def Drawtxt(self): # si le mode text ecrire un text dans le canvas
        self.Mytxt = self.entrer.get()
        self.myfont = font.Font (family="arial.ttf", size=self.size*10, weight='normal')
        self.canvas.create_text(self.txt_x, self.txt_y, text = self.Mytxt, font = self.myfont, fill = self.defaultclr)
        self.Mytxt = ""
        self.a.destroy()

    def select(self): # Si le mode selectionner l'utlisateur peut selectionner et deplacer
        # dans cet fonction il faut que l'utilisateur selection de haut vers le bas et de gauche vers droite
        if self.mode == "none":
            self.getoffset()
            if self.old_x and self.old_y:
                if self.moveselect == 0:
                    # s'il ya une selection dissiner un carre et sauvgarder la selection dans un ficher cacher
                    ImageGrab.grab((self.x_offset+self.old_x+9,  self.y_offset+self.old_y+149,
                                               self.x_offset+self.last_x+9, self.y_offset+self.last_y+149)).save("cacher_/slct.png")   
                    self.rectsel = self.canvas.create_rectangle(self.old_x,self.old_y,self.last_x,self.last_y, tags = "recsel")
                    self.moveselect, self.x_sel, self.y_sel, self.x2_sel, self.y2_sel = 1,self.old_x,self.old_y,self.last_x,self.last_y
                elif self.moveselect >= 1:
                    # s'il ya un mouvement a l'interieur de selection deplacer l'objet
                    if self.x_sel < self.old_x < self.x2_sel and self.y_sel < self.old_y < self.y2_sel:
                        if self.moveselect == 1:
                            self.canvas.itemconfig(self.rectsel,fill = self.defaultclr_2, outline = self.defaultclr_2)
                            self.imgsel = PhotoImage (file = "cacher_/slct.png")
                            self.canvas.create_image ( self.x_sel + (self.x2_sel-self.x_sel)/2, self.y_sel+ (self.y2_sel-self.y_sel)/2, image = self.imgsel, tags = "sel")
                        self.canvas.move("sel", self.last_x-self.old_x, self.last_y-self.old_y)
                        self.x_sel , self.y_sel , self.x2_sel, self.y2_sel = self.x_sel + (self.last_x - self.old_x), self.y_sel + (self.last_y - self.old_y), self.x2_sel + (self.last_x - self.old_x), self.y2_sel + (self.last_y - self.old_y)

                        self.moveselect += 1
                    else :
                        # s'il ya un mouvement a l'exterieur de la selection sauvgarder >
                        # et preparer pour une autre nouvel selection
                        if self.moveselect == 1:
                            self.canvas.delete('recsel')
                        self.Enregistrer_Sous("cacher_/myslct.png")
                        self.Ouvrir("cacher_/myslct.png")
                        self.moveselect = 0
                        os.remove("cacher_/slct.png")                    

    def reset(self, event): # returner au début et donner les valeurs par defaut
        self.last_x, self.last_y = event.x, event.y # les dernier x,y quand l'utlisateur laisse la click
        # voir s'il ya une fonction besoin des x,y dernier
        self.drawcarre()
        self.drawcircle()
        self.drawtriangle()
        self.drawline()
        self.select()
        #sinn returner tous au debut
        self.old_x, self.old_y = None, None
        self.last_x, self.last_y = None, None

    def detectclr (self, x, y):# detecteur de couleur
        self.getoffset()
        dc = windll.user32.GetDC(0)
        if self.Ecran_mode == "Simple": rgb = windll.gdi32.GetPixel(dc, x+self.x_offset+10, y+self.y_offset+178)
        else : rgb = windll.gdi32.GetPixel(dc, x, y+145)
        r = rgb & 0xff;     g = (rgb >> 8) & 0xff;      b = (rgb >> 16) & 0xff
        self.changerclr('#%02x%02x%02x' % (r, g, b))
    
    def rempliser (self): # s'il ya un forme activer activer le button de remplissage
        try :   self.canvas.itemconfig(self.ConfigObjet, fill = self.defaultclr_2)
        except : return
        
    def contObjet (self): # s'il ya un forme activer activer le button de contour
        try :   self.canvas.itemconfig(self.ConfigObjet, width = self.size,outline = self.defaultclr)
        except : return


if __name__ == '__main__':
    root = Tk()
    root.title("Paint")
    #root.iconbitmap(bitmap="lib/icone/iconepaint.png")
    app = Paint(root)
    root.geometry ("900x550")
    root.resizable(True, True)#root.resizable(width=False, height=False)
    root.mainloop()
