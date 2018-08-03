from urllib.request import urlopen, build_opener
from bs4 import BeautifulSoup

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers = ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10")

opener = build_opener()
opener.addheaders = [headers]
html = opener.open(url).read()
data = BeautifulSoup(html, "lxml")
print(data)

# html = urlopen(url)
# file = html.read()
# print(file)
