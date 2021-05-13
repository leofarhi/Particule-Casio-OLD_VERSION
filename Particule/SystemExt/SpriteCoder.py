from PIL import Image

def NameF(file):
    return file.split(".")[0]
def typeF(file):
    return file.split(".")[1]

is_array = lambda var: isinstance(var, (list, tuple))
def array_search(needle, haystack):
    try:
        return haystack.index(needle)
    except: return False
def array_push(valeurTableauPalette,rgb):
    valeurTableauPalette.append(rgb)
    return valeurTableauPalette
def ConvertImg(FileName,NameVar=None):
    _FILES=[FileName]
    StringReturn=[]
    _POST={"retourLigneSprite":"default","calculatrice":"G75/G85/G95/G35","bit":"",'tabpointeur':'oui','retourLigne':'oui','tabpointeur_name':'',"retourLigneSprite":"default"}
    nbFichier=len(_FILES); 
    for j,ActuFile in enumerate(_FILES):
        name = NameF(_FILES[j]);
        if (name!=''):
            extension = typeF(_FILES[j]);
            extension=extension.replace('image/','');
            valeurTableauPalette = [];
            
            im=Image.open(ActuFile)
            
            name=name.replace('.'+extension,'');
            largeur = im.size[0];
            hauteur = im.size[1];

            if NameVar==None:
                StringReturn += "{";
            else:
                StringReturn += "const unsigned char "+NameVar+"[]={";
            nbValeurSurUneLigne = 0;
            for y in range(hauteur):   
                if (_POST.get("retourLigneSprite")=="default" or _POST.get("retourLigneSprite")=="perso" and nbValeurSurUneLigne == 0 ):
                        StringReturn += "  ";
                codebinaire = '';
                for x in range(largeur):
                    try:r, g, b,_ = im.getpixel((x, y))
                    except:
                        try:r, g, b = im.getpixel((x, y))
                        except:
                            im=im.convert('RGB')
                            try:r, g, b,_ = im.getpixel((x, y))
                            except:r, g, b = im.getpixel((x, y))
                    
                    #r = (rgb >> 16) & 0xFF;
                    #g = (rgb >> 8) & 0xFF;
                    #b = rgb & 0xFF;

                    
                    if(_POST.get("calculatrice")=="G75/G85/G95/G35"):
                        moyennecouleur = (r+g+b)/3;
                        if (moyennecouleur<123):
                            codebinaire = codebinaire+'1';
                        else:
                            codebinaire = codebinaire+'0';
                        if (len(codebinaire)==8 or x+1 == largeur):
                            while(len(codebinaire)!=8):
                                codebinaire=codebinaire+'0';
                            hexa = int(str(codebinaire),2) #hexa = hex( int(str(codebinaire),2) );
                            StringReturn += hex(hexa)#"0x"+hexa;
                            nbValeurSurUneLigne+=1;
                            codebinaire='';
                            if (x+1 == largeur and y+1 == hauteur):
                                StringReturn += "";
                            else:
                                if (_POST.get("retourLigneSprite")=="default" or _POST.get("retourLigneSprite")=="uneLigne"):
                                    StringReturn += ",";
                                elif (_POST.get("retourLigneSprite")=="chaquevaleur"):
                                    StringReturn += ",";
                                else:
                                    StringReturn += ",";
                                    if nbValeurSurUneLigne >= intval(""+_POST.get("nbCaractere")+"") :
                                        nbValeurSurUneLigne = 0;
                                        if (x+1 != largeur):
                                                StringReturn += "";
                        else:
                            rgb = (( int(31*r/255) & 0x1F) << 11 ) | (( int(63*g/255) & 0x3F) << 5 ) | (( int(31*b/255) & 0x1F)) #rgb = (( (31*r/255) & 0x1F) << 11 ) | (( (63*g/255) & 0x3F) << 5 ) | (( (31*b/255) & 0x1F));
                            rgb = hex(rgb) #rgb = dechex(rgb);
                            if (_POST.get("bit")=="8bit"):
                                if (array_search(rgb,valeurTableauPalette) == False) and (type(array_search(rgb,valeurTableauPalette)) == type(False)):
                                    array_push(valeurTableauPalette,rgb);
                                    StringReturn += hex(array_search (rgb,valeurTableauPalette));
                                    nbValeurSurUneLigne+=1;
                                else:
                                    StringReturn += hex(array_search (rgb,valeurTableauPalette));
                                    nbValeurSurUneLigne+=1;
                            elif (_POST.get("bit")=="16bit"):
                                StringReturn += rgb#"0xrgb";
                                nbValeurSurUneLigne+=1;
                            if (x+1 == largeur and y+1 == hauteur):
                                StringReturn += "";
                            else:
                                if (_POST.get("retourLigneSprite")=="default" or _POST.get("retourLigneSprite")=="uneLigne"):
                                    StringReturn += ",";
                                elif (_POST.get("retourLigneSprite")=="chaquevaleur"):
                                    StringReturn += ",";
                                else:
                                    StringReturn += ",";
                                    if nbValeurSurUneLigne >= intval(""+_POST.get("nbCaractere")+""):
                                        nbValeurSurUneLigne = 0;
                                        if (x+1 != largeur):
                                            StringReturn += "";
                                                            
            if (_POST.get("retourLigneSprite")!="uneLigne"):
                StringReturn += "};";		
            else:
                StringReturn += "};";		

                
    #/************************************/
    #/** ici on code le tab de pointeur **/
    #/************************************/
    if (_POST.get('tabpointeur')=='oui' and _POST.get('tabpointeur_name')!=''):
        if (_POST.get("bit")=="8bit") or _POST.get("calculatrice")=="G75/G85/G95/G35":
            StringReturn += "const unsigned char* "+_POST.get('tabpointeur_name')+'[] = {';
            if (_POST.get('retourLigne')=='oui'):
                    StringReturn += "";
        else:
            StringReturn += "const color_t* "+_POST.get('tabpointeur_name')+'[] = {';
            if (_POST.get('retourLigne')=='oui'):
                    StringReturn += "";
        for j in range(nbFichier):
            name = NameF(_FILES[j]);
            name = name.replace('.png','');
            if (name!=''):
                StringReturn += name;
                if (j+1!=nbFichier):
                        StringReturn += ",";
                if (_POST.get('retourLigne')=='oui'):
                        StringReturn += "";

        if (_POST.get('retourLigne')=='oui'):
            StringReturn += "};";

        else:
            StringReturn += "};";
    a=""
    for i in StringReturn:a+=i
    StringReturn=a
    for i in range(len(StringReturn)):StringReturn=StringReturn.replace(",,",",").replace(" ,",",").replace("{,","{")
    return [StringReturn,im.size]
