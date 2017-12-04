from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# bsObj = BeautifulSoup(html, 'lxml')
book = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")

# print(html.read())
print(str(book.read(), 'utf-8'))
