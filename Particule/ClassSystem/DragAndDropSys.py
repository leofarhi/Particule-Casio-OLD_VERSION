from Particule import *
class DragAndDropSys:
    def __init__(self,Particule):
        self.Particule = Particule
        self.FameEvent = []
        self.Data = {}
        self.IsDarg = False
    def Drop(self,Data=None):
        if self.IsDarg:
            #print("Drop")
            if Data!=None:
                self.Data = Data
            mouseX,mouseY= self.Particule.Mafenetre.winfo_pointerx(), self.Particule.Mafenetre.winfo_pointery()
            for frame in self.FameEvent:
                fx,fy,fw,fh=frame.winfo_rootx(), frame.winfo_rooty(), frame.winfo_width(), frame.winfo_height()
                #print(fx,fy,fw,fh,mouseX,mouseY)
                if fx<=mouseX<=fx+fw and fy<=mouseY<=fy+fh:
                    frame.Drop(self.Data)
        self.Data = {}
        self.IsDarg = False
    def Drag(self,Data=None):
        #print("Drag")
        if Data != None:
            self.Data = Data
        self.IsDarg = True