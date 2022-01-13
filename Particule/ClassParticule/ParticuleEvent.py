import Particule
class ParticuleEvent:
    def __init__(self,ClassObject=None,Classfunction="",templateID="T"):
        self.ClassObject = ClassObject
        self.Classfunction = Classfunction
        self.templateID=templateID

    def get(self):
        GmID=None
        if self.ClassObject!=None:
            GmID = self.ClassObject.ID
        return (GmID,self.Classfunction,self.templateID)

    def set(self,ClassObject=None,Classfunction="",templateID="T"):
        self.ClassObject = ClassObject
        self.Classfunction = Classfunction
        self.templateID = templateID
