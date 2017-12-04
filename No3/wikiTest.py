from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())
pages = set()

def getLinks(articleUrl):
    '''
    返回的是一个序列数组
    :param articleUrl:
    :return:
    '''
    global pages
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 遇到了新页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("/wiki/Kevin_Bacon")

# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)

# for link in bsObj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
# for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
