from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

#html = urlopen("http://pythonscraping.com/pages/page1.html")  #可能会出现错误
#bsObj = BeautifulSoup(html.read(), "lxml")
#print(bsObj.body.h1)

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not found")
else:
    print(title)


