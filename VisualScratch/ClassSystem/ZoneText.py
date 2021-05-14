from VisualScratch import *
All_Word=[("def ","orange_tag"),
          ("class ","orange_tag"),
          ("with ","orange_tag"),
          ("open ","blue_tag"),
          ("self","blue_tag"),
          ("__init__","blue_tag"),
          ("if ","orange_tag"),
          ("else ","orange_tag"),
          ("while ","orange_tag")]
class ZoneText(Frame):
    def __init__(self,root,**kwargs):
        Frame.__init__(self,root,**kwargs)

        # self.MainTexte_var_Entry=StringVar()
        # self.MainTexte=Entry(self.Mafenetre,width=40,textvariable=self.MainTexte_var_Entry)
        self.MainTexte = Text(self, undo=True)  # ,textvariable=self.MainTexte_var_Entry)
        self.MainTexte.pack(fill=BOTH, expand=True, side=TOP)
        self.MainTexte.bind("<KeyPress>", self.WhenTextChange)
        self.SetColorTag()

    def WhenTextChange(self, even):
        self.ChangeColorAll()

    def GetMainTexte(self):
        return self.MainTexte.get("1.0", "end")

    def setTextInput(self, text):
        self.MainTexte.delete(1.0, "end")
        self.MainTexte.insert(1.0, text)

    def OpenFile(self):
        file = Fl.open_file()
        self.PathFile = file
        if file == "":
            return
        with open(file, 'r') as fic:
            self.setTextInput(fic.read())
        self.WhenTextChange("")

    def SaveFile(self, event=""):
        if self.PathFile == "":
            self.SaveAsFile()
            return
        self.SaveAll(self.PathFile)

    def SaveAsFile(self):
        file = Fl.save_file()
        self.PathFile = file
        self.SaveAll(self.PathFile)

    def NewFile(self):
        self.setTextInput("")
        self.SaveAsFile()

    def SaveAll(self, PathFile):
        if PathFile == "":
            return
        with open(PathFile, 'w') as fic:
            fic.write(self.GetMainTexte())



    def SetColorTag(self):
        self.MainTexte.tag_config("blue_tag", foreground="blue")
        self.MainTexte.tag_config("orange_tag", foreground="orange")

        self.MainTexte.tag_config("default_c", foreground="black")

    def ChangeColorAll(self):
        # self.MainTexte.tag_add("default_c", "1.0","end")
        for i in All_Word:
            self.ChangeColorOne(i[0], i[1])

    def ChangeColorOne(self, word, color):

        # word length use as offset to get end position for tag
        offset = '+%dc' % len(word)  # +5c (5 chars)

        # search word from first char (1.0) to the end of text (END)
        pos_start = self.MainTexte.search(word, '1.0', END)

        # check if found the word
        while pos_start:
            # create end position by adding (as string "+5c") number of chars in searched word
            pos_end = pos_start + offset

            # print pos_start, pos_end # 1.6 1.6+5c :for first `World`

            # add tag
            self.MainTexte.tag_add(color, pos_start, pos_end)

            # search again from pos_end to the end of text (END)
            pos_start = self.MainTexte.search(word, pos_end, END)
