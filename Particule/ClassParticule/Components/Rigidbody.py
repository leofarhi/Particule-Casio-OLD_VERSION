from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2


class Rigidbody(Component):
    def __init__(self, gameObject, **kwargs):
        Component.__init__(self, gameObject, __name__.split(".")[-1], **kwargs)
        self.Mass = 0
        self.UseGravity = False
        self.IsKinematic = False

        self.AttributVisible = ["Mass", "UseGravity", "IsKinematic", ]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)

        data.update({
            "Mass": self.Mass, "UseGravity": self.UseGravity, "IsKinematic": self.IsKinematic,
        })
        return data

    def LoadDataDict(self, data, component, dataCompo, dicoGameObject, dicoComponent):
        Component.LoadDataDict(self, data, component, dataCompo, dicoGameObject, dicoComponent)
        self.Mass = dataCompo["Mass"]
        self.UseGravity = dataCompo["UseGravity"]
        self.IsKinematic = dataCompo["IsKinematic"]


