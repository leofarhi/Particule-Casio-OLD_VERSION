from ClassSystem.EditorWindow import EditorWindow
class ProjectSettingsWindow(EditorWindow):
    def __init__(self, RootWindow):
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name":"Project Settings"},
                              Resize=False, ScrollbarShow=False)