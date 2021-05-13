#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from PIL import Image
import numpy as np
import pylab as pl
import matplotlib.cm as cm
import cv2 
import sys, os
def change_ext():
    for i in os.listdir():
        if ".jpg" in i:
            imgRep=i
            name=((imgRep).split("."))[0]
            extend=((imgRep).split("."))[1]
            frame=Image.open(imgRep)
            frame = frame.convert('1')
            frame.save("img/"+name+".bmp")
change_ext()
