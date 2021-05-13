from tkinter import *
from tkinter.messagebox import *
from SystemExt import File_Folder as Fl
from PIL import Image
import numpy as np
import pylab as pl
import matplotlib.cm as cm
import cv2 
import sys, os
FolderProject=os.getcwd()
def contour(newImg):
    #newImg = cv2.split(newImg)[0]
    newImg = cv2.Laplacian(newImg, cv2.CV_8U, ksize = 5)
    newImg = cv2.split(newImg)[0]
    #newImg = cv2.Canny(newImg, 300, 400)
    return newImg
def gray(im):
    im =Image.fromarray(im)
    im_grey = im.convert('L') # convert the image to *greyscale*
    im= im.convert('1')
    im_array = np.array(im_grey)
    #pl.imshow(im_array, cmap=cm.Greys_r)
    return im_array
def bitam(bitmap):
    # Split the three channels
    
    bitmap = np.dot((bitmap > 128).astype(float),255)
    im = Image.fromarray(bitmap.astype(np.uint8))
    return im
def arraylst(frame):
    a=np.array(frame)
    c=a.tolist()
    for ind,i in enumerate(c):
        for ind2,o in enumerate(i):
            if o==255:
                (c[ind])[ind2]=1
    return c
def create_line(lst):
    a=[]
    t=False
    z=[]
    for ind,i in enumerate(lst):
        for ind2,o in enumerate(i):
            if not o==1:
                if t==False:
                    z=[]
                    t=True
                    z.append(ind)
                    z.append(ind2)
            else:
                if t:
                    t=False
                    z.append(ind2)
                    Tz=z[2]-z[1]
                    if Tz<1:Tz=1
                    a.append([z[0],z[1],Tz])
                    z=[]
        if t:
            t=False
            z.append(ind2)
            Tz=z[2]-z[1]
            if Tz<1:Tz=1
            a.append([z[0],z[1],Tz])
            z=[]
    return a
def ImageCompile(file):
    img=Image.open(file)
    img = img.convert('1')
    img.save(file)
def ImageConvert(imgRep):
    scale_percent=50
    name=((imgRep.split("/")[-1]).split("."))[0]
    extend=((imgRep.split("/")[-1]).split("."))[1]
    frame=cv2.imread(imgRep,0)
    """
    int(frame.shape[1] * scale_percent / 100)
    int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    """
    if not extend=="bmp":
        frame=Image.open(imgRep)
        frame=np.array(frame)
        frame=contour(frame)
        frame=gray(frame)
        frame=bitam(frame)
    else:
        frame = Image.fromarray(frame.astype(np.uint8))
    frame=np.array(frame)
    if not extend=="bmp":
        frame = (255-frame)
    return frame
def ImportImage(rep,repDesti):
    scale_percent=50
    if rep==False:
        imgRep=Fl.open_file()
    else:
        imgRep=rep
    name=((imgRep.split("/")[-1]).split("."))[0]
    extend=((imgRep.split("/")[-1]).split("."))[1]
    frame=cv2.imread(imgRep,0)
    """
    int(frame.shape[1] * scale_percent / 100)
    int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    """
    if not extend=="bmp":
        frame=Image.open(imgRep)
        frame=np.array(frame)
        frame=contour(frame)
        frame=gray(frame)
        frame=bitam(frame)
    else:
        frame = Image.fromarray(frame.astype(np.uint8))
    frame=np.array(frame)
    if not extend=="bmp":
        frame = (255-frame)
    cv2.imwrite(repDesti, frame)
    return
