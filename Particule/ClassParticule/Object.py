class Object:
    def __init__(self,Particule,name="",hideFlags=True,UUID=False):
        self.Particule = Particule
        self.hideFlags = hideFlags
        self.name = name
        self.ID = self.Particule.CreateUUID(self,UUID)
    def UpdateOnGUI(self):
        pass
    def GetInstanceID(self):
        pass
    def ToString(self):
        return self.name
    def Destroy(self):
        if self.ID in self.Particule.All_UUID:
            del self.Particule.All_UUID[self.ID]
    def DestroyImmediate(self):
        pass
    def DontDestroyOnLoad(self):
        pass
    def FindObjectOfType(self):
        pass
    def FindObjectsOfType(self):
        pass
    def Instantiate(self):
        pass
