from Particule import *
from ClassSystem.EditorWindow import EditorWindow

class Animator(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self,RootWindow,Resize=True,ScrollbarShow=False)