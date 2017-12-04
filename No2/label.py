from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)

# for sibling in bsObj.find("table", attrs={"id": "giftList"}).tr.next_siblings: # 返回的是 "标签组" !!!
#     print(sibling)

print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
      )
