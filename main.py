"""
Inspiration from: 
https://gist.github.com/glof2/b490f5df1961d5d471271ae930aee316

and https://www.dataquest.io/blog/web-scraping-tutorial-python/
"""

import requests #gives acces to websites
from bs4 import BeautifulSoup  #bs gives nice structures to work with when scraping (understands html/css)
import ctypes  #allow to access user32.dll

url = "https://apod.nasa.gov/"

def changeWallpaper(newImage):
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, newImage , 0)
    
page = requests.get(url)        #makes a GET request to the web server hosting the website
soup=BeautifulSoup(page.content, 'html.parser')


    
    