"""
Inspiration from: 
https://gist.github.com/glof2/b490f5df1961d5d471271ae930aee316

and https://www.dataquest.io/blog/web-scraping-tutorial-python/
"""

import requests #gives acces to websites
from bs4 import BeautifulSoup  #bs gives nice structures to work with when scraping (understands html/css)
import ctypes  #allow to access user32.dll
import urllib.request #to download img
import os
import webbrowser

url = "https://apod.nasa.gov/"

def changeWallpaper(imagePath):
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, newImage , 0)
    
page = requests.get(url)        #makes a GET request to the web server hosting the website
soup=BeautifulSoup(page.content, 'html.parser')
#date = soup.findAll("p")[1].text.strip()
image = soup.find("img")
url += image["src"]
print(url)
webbrowser.open(url)

urllib.request.urlretrieve(url, "img_of_the_day.jpg")
pathToImg = os.path.normpath('C:\Users\PC\Desktop\gitProjects\personalAutomationMiniProjects\bkgrdPictureChange\img_of_the_day')
#pathToImg = 'C:\Users\PC\Desktop\gitProjects\personalAutomationMiniProjects\bkgrdPictureChange\img_of_the_day'
changeWallpaper(pathToImg)    