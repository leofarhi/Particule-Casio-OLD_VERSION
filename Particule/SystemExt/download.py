from bs4 import BeautifulSoup
from urllib import request
import urllib
import urllib3
import requests
import socket
import time
import sys
import os
import shutil
import io
import zipfile
import pygame as pg
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
rep=os.getcwd()
try:
    os.makedirs(rep+"//lib//temp_lib", exist_ok=True)
    shutil.rmtree(rep+"//lib//temp_lib")
    os.makedirs(rep+"//lib//temp_lib", exist_ok=True)
except:
    ""
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen
def web(url):
    http = urllib3.PoolManager()
    #print(url)

    try:
            response = requests.get(url)
            map_html = BeautifulSoup(response.content, "html.parser")
            map_html=str(map_html)
            map_html=map_html.replace("</string>","")
            try:
                map_html=map_html.decode("utf-8")
            except:
                ""
            map_html=map_html.replace("Ã©","é")
    except:
            map_html = (urlopen(url).read()).decode()
    return str(map_html)
def web_import_picture(url):
    image_url = url
    image_str = urlopen(image_url).read()
    image_file = io.BytesIO(image_str)
    image_file = pg.image.load(image_file)
    return image_file
def download(url,rep=rep):
    url=url.replace("/blob/","/raw/")
    a=urllib.request.urlretrieve(url)
    url=url.split("/")
    url=(url[-1]).replace("%20"," ")
    shutil.move(a[0],rep+"/"+url)
    return url

def LoadWeb(url):
    Data=web(url)
    Data=Data.split('<div class="topic-comments">')[1]
    Data=Data.split('<div class="align-center">')[0]
    Data=Data.split('<div class="topic-post')
    Data2=[]
    for i in Data:
        try:
            i=i.split(">Ajouté le")
        except:
            ""
        Data2=Data2+i
    return Data2
def Import(url,rep2):
    name=download(url,rep+"//lib//temp_lib")
    with zipfile.ZipFile(rep+"//lib//temp_lib//"+name, 'r') as zip_ref:
            zip_ref.extractall(rep2)
