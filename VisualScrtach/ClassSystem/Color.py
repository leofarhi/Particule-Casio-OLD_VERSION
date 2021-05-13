class Couleurs:
    bleu_fonce=(76,151,255)
    violet=(153,102,255)
    magenta=(207,99,207)
    jaune=(255,191,0)
    orange=(255,171,25)
    bleu_clair=(92,177,214)
    vert=(89,192,89)
    orange_fonce=(255,140,26)
    rose=(255,102,128)
    vert_fonce=(15,189,140)
    gris=(128,128,128)
    gris_clair=(208,208,208)
    noir=(0,0,0)

def color(colore):
    try:
        colore="#%02x%02x%02x" % colore
    except:
        pass
    return colore

def ConvertNameInvalid(name):
   NewName=""
   for Ind,char in enumerate(name):
      if (char.isalpha() or char.isalnum()):
         if (Ind==0 and char.isdecimal()):
            NewName+="V"
         NewName+=char
      else:
         NewName+="IvC"
   return NewName
def CorrigeBind(textvariable,event):
   pass#textvariable.set(ConvertNameInvalid(textvariable.get()))