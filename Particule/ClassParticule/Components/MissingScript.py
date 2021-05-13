from Particule import *
from ClassParticule.Component import Component
class MissingScript(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self, gameObject, __name__.split(".")[-1],**kwargs)

    def UpdateOnGUI(self):
        self.Destroy()