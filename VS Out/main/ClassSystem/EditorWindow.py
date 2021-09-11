from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk

class EditorWindow(Frame):#(WinFrameBas):
    def __init__(self,RootWindow,ExternalWindow=None,**kwargs):
        Frame.__init__(self,RootWindow,**kwargs)
        self.Sys = RootWindow.Sys
        self.RootWindow = RootWindow
        Frame.__init__(self,RootWindow)
        self.bind("<FocusIn>", self.OnFocus)
        self.bind("<FocusOut>", self.OnLostFocus)
    def destroy(self):
        Frame.destroy(self)

    def autoRepaintOnSceneChange(self):#Properties
        """
        La fenêtre est-elle automatiquement repeinte chaque fois que la scène a changé?
        :return:
        """
        pass
    def docked(self):#Properties
        """
        Renvoie true si EditorWindow est ancré.
        :return:
        """
        pass
    def hasFocus(self):#Properties
        """
        Renvoie true si EditorWindow est focalisé.
        :return:
        """
        pass
    def hasUnsavedChanges(self):#Properties
        """
        Lorsqu'il est défini sur true dans une classe dérivée, l'éditeur invite l'utilisateur à enregistrer les modifications non enregistrées si la fenêtre est sur le point d'être fermée.
        :return:
        """
        pass
    def maximized(self):#Properties
        """
        Cette fenêtre est-elle maximisée?
        :return:
        """
        pass
    def maxSize(self):#Properties
        """
        La taille maximale de cette fenêtre.
        :return:
        """
        pass
    def minSize(self):#Properties
        """
        La taille minimale de cette fenêtre.
        :return:
        """
        pass
    def position(self):#Properties
        """
        La position souhaitée de la fenêtre dans l'espace écran.
        :return:
        """
        pass
    def rootVisualElement(self):#Properties
        """
        Récupère l'élément visuel racine de cette hiérarchie de fenêtres.
        :return:
        """
        pass
    def saveChangesMessage(self):#Properties
        """
        Le message qui s'affiche à l'utilisateur s'il est invité à enregistrer
        :return:
        """
        pass
    def titleContent(self):#Properties
        """
        GUIContent utilisé pour dessiner le titre de EditorWindows.
        :return:
        """
        pass
    def wantsLessLayoutEvents(self):#Properties
        """
        Spécifie si une passe de mise en page est effectuée avant tous les événements utilisateur (par exemple, EventType.MouseDown ou [[EventType, KeyDown]]), ou est effectuée uniquement avant les événements de repeinture.
        :return:
        """
        pass
    def wantsMouseEnterLeaveWindow(self):#Properties
        """
        Vérifie si les événements MouseEnterWindow et MouseLeaveWindow sont reçus dans l'interface graphique de cette fenêtre de l'éditeur.
        :return:
        """
        pass
    def wantsMouseMove(self):#Properties
        """
        Vérifie si les événements MouseMove sont reçus dans l'interface graphique de cette fenêtre de l'éditeur.
        :return:
        """
        pass
    def BeginWindows(self):#Public Methods
        """
        Marquez la zone de début de toutes les fenêtres contextuelles.
        :return:
        """
        pass
    def Close(self):#Public Methods
        """
        Fermez la fenêtre de l'éditeur.
        :return:
        """
        pass
    def EndWindows(self):#Public Methods
        """
        Fermez un groupe de fenêtres démarré avec EditorWindow.BeginWindows.
        :return:
        """
        pass
    def Focus(self):#Public Methods
        """
        Déplace le focus clavier vers un autre EditorWindow.
        :return:
        """
        pass
    def GetExtraPaneTypes(self):#Public Methods
        """
        Obtient les volets supplémentaires associés à la fenêtre.
        :return:
        """
        pass
    def RemoveNotification(self):#Public Methods
        """
        Arrêtez d'afficher le message de notification.
        :return:
        """
        pass
    def Repaint(self):#Public Methods
        """
        Faites repeindre la fenêtre.
        :return:
        """
        pass
    def SaveChanges(self):#Public Methods
        """
        Effectue une action de sauvegarde sur le contenu de la fenêtre.
        :return:
        """
        pass
    def SendEvent(self):#Public Methods
        """
        Envoie un événement à une fenêtre.
        :return:
        """
        pass
    def Show(self):#Public Methods
        """
        Affichez la fenêtre EditorWindow.
        :return:
        """
        pass
    def ShowAsDropDown(self):#Public Methods
        """
        Affiche une fenêtre avec un comportement et un style de liste déroulante.
        :return:
        """
        pass
    def ShowAuxWindow(self):#Public Methods
        """
        Affichez la fenêtre de l'éditeur dans la fenêtre auxiliaire.
        :return:
        """
        pass
    def ShowModal(self):#Public Methods
        """
        Afficher la fenêtre de l'éditeur modal.
        :return:
        """
        pass
    def ShowModalUtility(self):#Public Methods
        """
        Affichez EditorWindow sous la forme d'une fenêtre modale flottante.
        :return:
        """
        pass
    def ShowNotification(self):#Public Methods
        """
        Afficher un message de notification.
        :return:
        """
        pass
    def ShowPopup(self):#Public Methods
        """
        Affiche une fenêtre de l'éditeur utilisant un encadrement de style popup.
        :return:
        """
        pass
    def ShowUtility(self):#Public Methods
        """
        Affichez EditorWindow sous la forme d'une fenêtre utilitaire flottante.
        :return:
        """
        pass
    def CreateWindow(self):#Static Methods
        """
        Crée une EditorWindow de type T.
        :return:
        """
        pass
    def FocusWindowIfItsOpen(self):#Static Methods
        """
        Concentre le premier EditorWindow trouvé du type spécifié s'il est ouvert.
        :return:
        """
        pass
    def GetWindow(self):#Static Methods
        """
        Renvoie le premier EditorWindow de type t actuellement à l'écran.
        :return:
        """
        pass
    def GetWindowWithRect(self):#Static Methods
        """
        Renvoie le premier EditorWindow de type t actuellement à l'écran.
        :return:
        """
        pass
    def HasOpenInstances(self):#Static Methods
        """
        Vérifie si une fenêtre d'éditeur est ouverte.
        :return:
        """
        pass
    def Awake(self):#Messages
        """
        Appelé lorsque la nouvelle fenêtre est ouverte.
        :return:
        """
        pass
    def CreateGUI(self):#Messages
        """
        CreateGUI est appelé lorsque rootVisualElement de EditorWindow est prêt à être rempli.
        :return:
        """
        pass
    def hasUnsavedChanges(self):#Messages
        """
        Lorsqu'il est défini sur true dans une classe dérivée, l'éditeur invite l'utilisateur à enregistrer les modifications non enregistrées si la fenêtre est sur le point d'être fermée.
        :return:
        """
        pass
    def OnDestroy(self):#Messages
        """
        OnDestroy est appelé pour fermer la fenêtre EditorWindow.
        :return:
        """
        pass
    def OnFocus(self,event=None):#Messages
        """
        Appelé lorsque la fenêtre obtient le focus clavier.
        :return:
        """
        pass
    def OnGUI(self):#Messages
        """
        Implémentez votre propre interface graphique d'éditeur ici.
        :return:
        """
        pass
    def OnHierarchyChange(self):#Messages
        """
        Gestionnaire de message envoyé lorsqu'un objet ou un groupe d'objets de la hiérarchie change.
        :return:
        """
        pass
    def OnInspectorUpdate(self):#Messages
        """
        OnInspectorUpdate est appelé à 10 images par seconde pour donner à l'inspecteur une chance de se mettre à jour.
        :return:
        """
        pass
    def OnLostFocus(self,event=None):#Messages
        """
        Appelé lorsque la fenêtre perd le focus clavier.
        :return:
        """
        pass
    def OnProjectChange(self):#Messages
        """
        Gestionnaire de message envoyé chaque fois que l'état du projet change.
        :return:
        """
        pass
    def OnSelectionChange(self):#Messages
        """
        Appelé chaque fois que la sélection a changé.
        :return:
        """
        pass
    def saveChangesMessage(self):#Messages
        """
        Le message qui s'affiche à l'utilisateur s'il est invité à enregistrer
        :return:
        """
        pass
    def Update(self):#Messages
        """
        Appelé plusieurs fois par seconde sur toutes les fenêtres visibles.
        :return:
        """
        pass
