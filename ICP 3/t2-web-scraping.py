# to import required modules
import requests
from bs4 import BeautifulSoup
import os

# use request with get function to assign the web page content to htmlPage variable
htmlPage = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
bsObj = BeautifulSoup(htmlPage.content, "html.parser")
print("Title is: ", bsObj.title.string)
print("links in ", bsObj.title.string, ": ")
for link in bsObj.find_all('a'):
    print(link.get('href'))

