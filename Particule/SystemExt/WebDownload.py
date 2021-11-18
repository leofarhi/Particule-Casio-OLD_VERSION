from urllib import request
import urllib
import io
import urllib3
import requests
import shutil
from bs4 import BeautifulSoup
import codecs,os,sys
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen
def web(url):
    http = urllib3.PoolManager()
    response = requests.get(url)
    code = BeautifulSoup(response.content, "html.parser")
    code=str(code)
    code=code.replace("</string>","")
    code=code.replace("Ã©","é")
    return code
def DownloadFile(url,rep):
    a=urllib.request.urlretrieve(url)
    shutil.move(a[0],rep)
