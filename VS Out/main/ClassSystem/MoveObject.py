from ClassSystem.Scratch import *
class MoveObject:
    def __init__(self,WindCanvas):
        self.WindCanvas = WindCanvas
        self.X = 0
        self.Y = 0
        self.canevas = self.WindCanvas.MainCanvas
        self.WidgetIsDrabed = False
        self.DragAndInOtherBlock = False
        self.LastMclicX = None
        self.LastMclicY = None

    def ClicDuMilleu(self, event):
        self.LastMclicX = event.x
        self.LastMclicY = event.y

    def ClicDuMilleuDrag(self, event):
        X = event.x
        Y = event.y
        self.X = X
        self.Y = Y
        if self.WindCanvas.CamX + (X - self.LastMclicX) >= 0:
            X -= abs(self.WindCanvas.CamX + (X - self.LastMclicX))
        if self.WindCanvas.CamY + (Y - self.LastMclicY) >= 0:
            Y -= abs(self.WindCanvas.CamY + (Y - self.LastMclicY))
        self.WindCanvas.MoveAll(self.LastMclicX, self.LastMclicY, X, Y)
        self.WindCanvas.CamX = self.WindCanvas.CamX + (X - self.LastMclicX)
        self.WindCanvas.CamY = self.WindCanvas.CamY + (Y - self.LastMclicY)
        self.LastMclicX = X
        self.LastMclicY = Y

    def Clic(self, event):
        self.canevas.focus_set()
        self.LastMclicX = event.x
        self.LastMclicY = event.y
        self.X = self.LastMclicX
        self.Y = self.LastMclicY
        maxTemp = 0
        for i in list(self.WindCanvas.AllWidget.values()):
            if i == None: continue
            temp = i.TypeForme in self.WindCanvas.FormeParametre
            [xmin, ymin, xmax, ymax] = i.BoxCollider[0]
            if xmin <= self.LastMclicX <= xmax and ymin <= self.LastMclicY <= ymax:
                for A in i.GroupeWidget:
                    for W in A:
                        if type(W) == int and W > maxTemp:
                            self.WidgetIsDrabed = i
                            maxTemp = W

    def Drag(self, event):
        X = event.x
        Y = event.y
        if X < 0:
            return  # X = self.LastMclicX
        if Y < 0:
            return  # Y = self.LastMclicY
        if self.WidgetIsDrabed == False:
            return
        if self.WidgetIsDrabed.ParentBlock != None:
            if self.WidgetIsDrabed.TypeForme in self.WindCanvas.FormeParametre:
                tempObj = self.WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock)
                for ind2, o in enumerate(tempObj.GroupeParametre):
                    if o[1] == self.WidgetIsDrabed.WidgetIndex:
                        (tempObj.GroupeParametre[ind2])[1] = None
                        tempObj.update()
                        break
            else:
                tempNb = self.WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock).NextBlockIn.index(
                    self.WidgetIsDrabed.WidgetIndex)
                self.WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock).NextBlockIn[tempNb] = None
                self.WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock).update()
            self.WidgetIsDrabed.ParentBlock = None

        # print(self.WidgetIsDrabed.NextBlockIn)

        self.DragAndInOtherBlock = False
        for ind, i in enumerate(list(self.WindCanvas.AllWidget.values())):
            if i == None or i == self.WidgetIsDrabed: continue
            if ind != self.WidgetIsDrabed.WidgetIndex:
                for ind2, o in enumerate(i.BoxCollider):
                    [xmin, ymin, xmax, ymax] = o
                    if xmin <= self.X <= xmax and ymin <= self.Y <= ymax:
                        self.DragAndInOtherBlock = i
                        self.NbBoxCollider = ind2
        self.WindCanvas.MoveWidget(self.WidgetIsDrabed, self.LastMclicX, self.LastMclicY, X, Y)
        if self.WidgetIsDrabed != False:
            self.WidgetIsDrabed.update()
        self.LastMclicX = X
        self.LastMclicY = Y
        self.X = X
        self.Y = Y

    def Drop(self, event):
        Done = False
        if self.WidgetIsDrabed != False:
            if self.WidgetIsDrabed.TypeForme in self.WindCanvas.FormeParametre:
                for ind, i in enumerate(list(self.WindCanvas.AllWidget.values())):
                    if Done: break
                    if i == None or i == self.WidgetIsDrabed: continue
                    for ind2, o in enumerate(i.BoxColiParametre):
                        # print(i.GroupeParametre,i.BoxColiParametre,ind2,i.WidgetIndex)
                        if Done: break
                        if (i.GroupeParametre[ind2])[0] == self.WidgetIsDrabed.TypeParametreSyc:
                            [xmin, ymin, xmax, ymax] = o
                            if xmin <= self.X <= xmax and ymin <= self.Y <= ymax:
                                if (i.GroupeParametre[ind2])[1] != None: continue
                                (i.GroupeParametre[ind2])[1] = self.WidgetIsDrabed.WidgetIndex
                                self.WidgetIsDrabed.ParentBlock = i.WidgetIndex
                                Done = True
                                break
        if 10 <= event.x <= 60 and 10 <= event.y <= 60 and self.WidgetIsDrabed != False:
            self.WidgetIsDrabed.RemoveSelf()
            self.WidgetIsDrabed = False
        else:
            if self.DragAndInOtherBlock != False and self.WidgetIsDrabed != False:
                # print("ok")
                # print(self.DragAndInOtherBlock.CanAddBlock,self.WidgetIsDrabed.CanPutInBlock)
                if self.DragAndInOtherBlock.CanAddBlock == True and self.WidgetIsDrabed.CanPutInBlock == True:
                    # print(self.NbBoxCollider,self.DragAndInOtherBlock.NextBlockIn)
                    if self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider] != None:
                        tempB = self.WindCanvas.AllWidget.get(self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider])

                        self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider] = None
                        tempB.ParentBlock = None

                        self.WindCanvas.MoveWidget(tempB, tempB.x, tempB.y, tempB.x + 20, tempB.y + 20)
                        tempB.update()

                    # self.DragAndInOtherBlock.GroupeWidget+=self.WidgetIsDrabed.GroupeWidget
                    self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider] = self.WidgetIsDrabed.WidgetIndex
                    self.WidgetIsDrabed.ParentBlock = self.DragAndInOtherBlock.WidgetIndex

        self.FrontPlanObject()
        if self.WidgetIsDrabed != False:
            self.WidgetIsDrabed.update()
        self.WidgetIsDrabed = False
        self.DragAndInOtherBlock = False
        MoveObjetDobe = True

    def FrontPlanObject(self):
        for Widget in list(self.WindCanvas.AllWidget.values()):
            if Widget == None: continue
            if Widget.TypeForme == "Encadrement":
                Widget.update()
        for Widget in list(self.WindCanvas.AllWidget.values()):
            if Widget == None: continue
            if Widget.TypeForme in self.WindCanvas.ListFormeInFront:
                Widget.update()