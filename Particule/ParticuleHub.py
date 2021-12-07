from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
import tkinter as tk
from tkinter import simpledialog
from tkinter.messagebox import *

from Particule import *
from SystemExt.WebDownload import *
import patoolib
import subprocess
import os
import platform

class ButtonInstall(tk.Frame):
    def __init__(self,frame,text="",command=print, *args, **kwargs):
        tk.Frame.__init__(self,frame,width=20, height=5)
        self.command = command
        self.Button = Button(self,text=TradTxt(text),width=20, height=5,command=self.start)
        self.Button.pack(fill=BOTH)
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()

    def start(self):
        self.progress["value"] = 0
        self.progress["maximum"] = 100
        self.command()

class ParticuleHub:
    def __init__(self):
        self.Start = False
        self.RootHub = Tk()
        self.RootHub.title('Particule - Hub')
        self.RootHub.resizable(False, False)
        self.RootHub.grid_columnconfigure(0, weight=1)
        self.RootHub.grid_rowconfigure(0, weight=1)
        self.w = int(GetSystemMetrics(0) * 0.5)
        self.h = int(GetSystemMetrics(1) * 0.5)
        self.RootHub.geometry(str(self.w) + "x" + str(self.h))
        if Game_OS == "linux":
            try:
                self.RootHub.iconbitmap('@lib/logo.xbm')
            except:
                pass
            try:
                tempimg = tkinter.PhotoImage(file='lib/logo.png')
                self.RootHub.tk.call('wm', 'iconphoto', self.RootHub._w, tempimg)
            except:
                pass
        else:
            try:
                self.RootHub.iconbitmap('lib/logo.ico')
            except:
                pass

        self.BarreOnTop()
        self.FrameMain = Frame(self.RootHub)
        self.FrameMain.pack(fill=BOTH, expand=True, side=LEFT)

        self.Onglets()

        self.WinMain = LabelFrame(self.FrameMain)
        self.WinMain.pack(fill=BOTH, expand=True, side=LEFT)

        self.WinProjet()

        self.RootHub.mainloop()

    def NewProject(self,Folder=None):
        if Folder==None:
            Folder = self.AddProject()
        M.create_rep(Folder+ "/Assets")
        M.create_rep(Folder + "/Assets/MyAsset")
        M.create_rep(Folder + "/Library")
        M.create_rep(Folder + "/Library/ImagesBmpCache")
        M.create_rep(Folder + "/Library/ScriptEditor")
        M.create_rep(Folder + "/Library/lib")
        M.create_rep(Folder + "/Package")
        M.create_rep(Folder + "/ProjectSettings")
        M.create_rep(Folder + "/Temp")
        M.create_rep(Folder + "/Temp/Compile")
        M.create_rep(Folder + "/SLN")
        shutil.copyfile("lib/vide.png", Folder + "/Library/lib/vide.png")
        templst = os.listdir(Folder + "/ProjectSettings")
        if not "MainIcon.bmp" in templst:
            shutil.copyfile("lib/IconCalculatrice/MainIcon.bmp", Folder + "/ProjectSettings/MainIcon.bmp")
        if not "icon-sel.png" in templst:
            shutil.copyfile("lib/IconCalculatrice/icon-sel.png", Folder + "/ProjectSettings/icon-sel.png")
        if not "icon-uns.png" in templst:
            shutil.copyfile("lib/IconCalculatrice/icon-uns.png", Folder + "/ProjectSettings/icon-uns.png")

    def EditScriptBlock(self):
        self.RootHub.resizable(True, True)
        TempFrame = Frame(self.WinMain)
        TempFrame.pack(fill=BOTH, expand=True, side=LEFT)
        CSBT = AddBlockTk.CreateScriptBlockTk()
        CSBT.CreateBlockInFile(TempFrame)

    def BarreOnTop(self):
        Cheight = int(self.h * 0.1)
        self.CbarreTop = Canvas(self.RootHub, height=Cheight, bg="white")
        self.CbarreTop.pack(fill=X)
        self.img = Image.open("lib/LogoText.png")
        Wimg, Himg = self.img.size
        Wimg, Himg = int(Wimg * (Cheight / Himg)), int(Himg * (Cheight / Himg))
        self.img = self.img.resize((Wimg, Himg))  # , Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)
        self.CbarreTop.create_image(0, 0, anchor=NW, image=self.photo)

    def WinLearn(self):
        TempFrame = Frame(self.WinMain)
        TempFrame.pack(fill=BOTH, expand=True, side=LEFT)
        BoutonLearn = Button(TempFrame, text=TradTxt("Aller à la vidéo"), width=20, height=5,
                             command=partial(webbrowser.open, "https://youtu.be/WSUmLMhd7HQ"))
        BoutonLearn.pack(fill=X)
        # webbrowser.open('http://www.python.org')

    def WinInstall(self):
        TempFrame = Frame(self.WinMain)
        TempFrame.pack(fill=BOTH, expand=True, side=LEFT)
        if platform.system()=='Windows':
            BoutonInstallerSDK = ButtonInstall(TempFrame, text=TradTxt("Installer SDK Graph 75 85 95"), width=20, height=5,
                                 command=self.DownloadSdkCasio)
            BoutonInstallerSDK.grid(row=0, column=0)
        BoutonInstallerGint = ButtonInstall(TempFrame, text=TradTxt("Installer Gint"), width=20, height=5,
                                    command=self.DownloadGint)
        #BoutonInstallerGint.grid(row=0, column=1)
        # webbrowser.open('http://www.python.org')

    def ChangeOnglet(self, WinFrame):
        self.WinMain.destroy()
        self.WinMain = LabelFrame(self.FrameMain)
        self.WinMain.pack(fill=BOTH, expand=True, side=LEFT)
        WinFrame()

    def Onglets(self):
        self.Options = Frame(self.FrameMain, width=int(self.w * 0.2))
        self.Options.pack(side=LEFT, fill=Y)  # fill = BOTH, expand = True,side=LEFT)
        self.Options.configure(width=int(self.w * 0.2))
        self.BoutonProjet = Button(self.Options, text=TradTxt("Projets"), width=20, height=5,
                                   command=partial(self.ChangeOnglet, self.WinProjet))
        self.BoutonProjet.pack(fill=X)
        self.BoutonLearn = Button(self.Options, text=TradTxt("Apprendre"), width=20, height=5,
                                  command=partial(self.ChangeOnglet, self.WinLearn))
        self.BoutonLearn.pack(fill=X)

        self.BoutonInstalls = Button(self.Options, text=TradTxt("Installs"), width=20,
                                  height=5, command=partial(self.ChangeOnglet,self.WinInstall))
        self.BoutonInstalls.pack(fill=X)

        #self.BoutonLearn = Button(self.Options, text="Add ScriptBlock", width=20, height=5,
        #                          command=partial(self.ChangeOnglet, self.EditScriptBlock))
        # self.BoutonLearn.pack(fill = X)

    def Compoframeconfig(self, event):
        self.FWinProjetCanvasScroll.configure(
            scrollregion=self.FWinProjetCanvasScroll.bbox("all"))  # ,width=200,height=200)

    def AddProject(self):
        global _i
        rep = Fl.open_folder()
        LstProjects = rf.GetList("setup.txt", "AllProjects")
        LstProjects.append([rep.split("/")[-1], rep])
        rf.save("setup.txt", "AllProjects", str(LstProjects))
        self.FrameWinProjet.destroy()
        self.WinProjet()
        return rep

    def BouttonOpen(self, Data):
        rf.save("setup.txt", "FolderProject", str(Data[1]))
        self.NewProject(Data[1])
        self.Start = True
        self.RootHub.destroy()

    def DelProject(self, Data):
        global _i
        LstProjects = rf.GetList("setup.txt", "AllProjects")
        LstProjects.remove(Data)
        rf.save("setup.txt", "AllProjects", str(LstProjects))
        self.FrameWinProjet.destroy()
        self.WinProjet()

    def WinProjet(self):
        global _i
        self.FrameWinProjet = Frame(self.WinMain)
        self.FrameWinProjet.pack(fill=BOTH, expand=True, side=LEFT)
        self.FrameBoutton = Frame(self.FrameWinProjet)
        self.FrameBoutton.pack(side=TOP, fill=X)

        self.BoutonNew = Button(self.FrameBoutton, text=TradTxt("Nouveau Projet"), bg="#2297f3", fg="white",
                                command=self.NewProject)
        self.BoutonNew.pack(side=RIGHT, padx=5, pady=5)

        self.BoutonAdd = Button(self.FrameBoutton, text=TradTxt("Ajouter un Projet"), bg="#2297f3", fg="white",
                                command=self.AddProject)
        self.BoutonAdd.pack(side=RIGHT, padx=5, pady=5)

        self.FWinProjet = LabelFrame(self.FrameWinProjet, text="Projets")  # ,width=50,height=100,bd=1)
        self.FWinProjet.pack(fill=BOTH, expand=True, side=LEFT)

        self.FWinProjetCanvasScroll = Canvas(self.FWinProjet)

        self.AllWinProjetframe = Frame(self.FWinProjetCanvasScroll)

        self.CompoScroll = Scrollbar(self.FWinProjet, orient="vertical", command=self.FWinProjetCanvasScroll.yview)
        self.FWinProjetCanvasScroll.configure(yscrollcommand=self.CompoScroll.set)

        self.CompoScroll.pack(side="right", fill="y")
        self.FWinProjetCanvasScroll.pack(side="left", fill="both", expand=True)

        self.FWinProjetCanvasScroll.create_window((0, 0), window=self.AllWinProjetframe, anchor='nw',
                                                  width=int(self.w * 0.75))
        self.AllWinProjetframe.bind("<Configure>", self.Compoframeconfig)

        LstProjects = rf.GetList("setup.txt", "AllProjects")
        if LstProjects == False:
            rf.save("setup.txt", "AllProjects", "[]")
            LstProjects = []
        else:
            for i in LstProjects:
                FrameLstP = LabelFrame(self.AllWinProjetframe, bg="white")  # ,width = self.FWinProjet.winfo_width())
                FrameLstP.pack(fill=X, side=TOP)  # , padx = 5, pady = 5,anchor='nw')#,fill = X)
                FrameLstPLabel = Frame(FrameLstP, bg="white")
                FrameLstPLabel.pack(side=LEFT)
                LabelLstP = Label(FrameLstPLabel, text=i[0], justify="left", bg="white")
                LabelLstP.grid(row=0, column=0, sticky="w")

                LabelLstPRep = Label(FrameLstPLabel, text=i[1], justify="left", bg="white")
                LabelLstPRep.grid(row=1, column=0, sticky="w")

                bouttonDel = Button(FrameLstP, text=TradTxt("Retirer"), command=partial(self.DelProject, i))
                bouttonDel.pack(side=RIGHT, padx=5, pady=5)

                bouttonOuvrir = Button(FrameLstP, text=TradTxt("Ouvrir"), command=partial(self.BouttonOpen, i))
                bouttonOuvrir.pack(side=RIGHT, padx=5, pady=5)

    def DownloadSdkCasio(self):
        reponse = askyesno("Confirmation","Etes-vous sûr de vouloir installer SDK Casio ?")
        if not reponse:return
        text='''Lors de l'installation, ne le mettez pas dans un dossier avec des parenthèses tel que "Program Files (x86)" !'''
        url ="https://www.planet-casio.com/Fr/logiciels/dl_logiciel.php?id=76&file=1"
        rep = os.getcwd()+"/lib/temp_lib/sdk85.rar"
        repDir = os.getcwd() + "/lib/temp_lib/sdk85"
        DownloadFile(url,rep)
        print(rep)
        patoolib.extract_archive(rep, outdir=repDir)
        repDir+"/fx9860g_sdk/fx-9860G SDK setup.exe"
        showinfo("Important", text)
        os.startfile(repDir+"/fx9860g_sdk/fx-9860G SDK setup.exe")

    def DownloadGint(self):
        folder_path = os.getcwd() + "/lib/GintLib"
        if os.path.exists(folder_path):
            os.system('rmdir /S /Q "{}"'.format(folder_path))
        M.create_rep(folder_path)
        urls=["https://ftp.gnu.org/gnu/binutils/binutils-2.37.tar.xz","https://gcc.gnu.org/pub/gcc/releases/gcc-11.2.0/gcc-11.2.0.tar.xz"]
        DownloadFile(urls[0], folder_path+"/binutils-2.37.tar.xz")
        DownloadFile(urls[1], folder_path + "/gcc-11.2.0.tar.xz")
        repbat = os.path.abspath(folder_path).replace("\\","/")
        txt=self.BatFile(repbat)
        with open(repbat+"/InstallGint.bat","w") as fic:
            fic.write(txt)


    def BatFile(self,rep):
        return """cd """+rep+"""
export PREFIX="/mnt/"""+rep.replace("C:/Users","c/Users")+"""/opt/sh-elf-2.32-9.2.0"
wsl mkdir -p $PREFIX
cd """+rep+"""/opt/sh-elf-2.32-9.2.0
wsl export PATH="$PATH:$PREFIX/bin"
wsl echo "export PATH=\"\$PATH:$PREFIX/bin\"" >> $HOME/.profile
wsl echo "export PATH=\"\$PATH:$PREFIX/bin\"" >> $HOME/.bashrc
wsl tar -xJf binutils-2.37.tar.xz
wsl tar -xJf gcc-11.2.0.tar.xz
wsl mkdir build-binutils build-gcc
cd build-binutils
wsl apt-get update
wsl sudo apt install build-essential
wsl apt-get update
wsl sudo apt-get install libmpfr-dev
wsl sudo apt-get install libmpc-dev
wsl sudo apt-get install libgmp-dev
wsl ../binutils-2.37/configure --prefix=$PREFIX --target=sh3eb-elf
wsl --with-multilib-list=m3,m4-nofpu --disable-nls --program-prefix=sh-elf-
wsl make
wsl make install
cd ..
cd build-gcc/
wsl ../gcc-11.2.0/configure --target=sh3eb-elf --prefix=$PREFIX --disable-nls --enable-languages=c,c++ --without-headers
wsl make -j4 all-gcc
wsl make install-gcc
wsl make all-target-libgcc
wsl make install-target-libgcc
wsl git config --global http.sslverify false
cd ..
wsl git clone 'https://gitea.planet-casio.com/Lephenixnoir/fxsdk.git'
cd fxsdk
wsl sudo apt-get install libusb-0.1-4
wsl sudo apt-get install libusb-1.0
wsl sudo apt-get install 'libpng*'
wsl sudo apt update
wsl sudo apt install software-properties-common
wsl sudo add-apt-repository ppa:deadsnakes/ppa
wsl sudo apt install python3.7
wsl apt install python3-pip
wsl pip3 install Pillow
wsl pip3 install libusb
wsl pip3 install libusb1
wsl pip3 install --upgrade pip
wsl pip install --upgrade pip setuptools wheel
wsl pip3 install --upgrade pip setuptools wheel
wsl sudo apt-get install libxml2-dev libxmlsec1-dev
wsl sudo apt-get install -y udisks2
wsl sudo apt install pkg-config
wsl apt install cmake
wsl sudo apt-get install libglib2.0-dev
wsl wget http://www.libsdl.org/release/SDL2-2.0.9.tar.gz
wsl tar -xzvf SDL2-2.0.9.tar.gz
cd SDL2-2.0.9
wsl ./configure
wsl sudo make all
wsl sudo apt install curl git python3 build-essential cmake
wsl sudo pacman -S curl git python3 gcc make cmake
wsl curl "https://gitea.planet-casio.com/Lephenixnoir/GiteaPC/raw/branch/master/install.sh" -o /tmp/giteapc-install.sh && bash /tmp/giteapc-install.sh
wsl sudo apt install libudisks2-dev
cd ..
wsl sudo apt install cmake libsdl2-dev g++
wsl cmake -B build
wsl giteapc install Lephenixnoir/fxsdk Lephenixnoir/gint

set /p DUMMY=Hit ENTER to continue...
runas /user:# "" >nul 2>&1"""
