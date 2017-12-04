from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     unix_socket='/var/run/mysqld/mysqld.sock',
#     user='root',
#     passwd='123',
#     db='scraping')
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM pages WHERE id=1;")
# print(cur.fetchone())
#
# cur.close()
# conn.close()

conn = pymysql.connect(
    host='127.0.0.1',
    unix_socket='/var/run/mysqld/mysqld.sock',
    user='root',
    passwd='123',
    db='mysql',
    charset='utf8'
)
cur = conn.cursor()
cur.execute("USE scraping") # 这句 code 可以通过在 db='scraping' 来取消

random.seed(datetime.datetime.now())

def store(title, content):
    '''
    将 网页的数据 存储到本地的 mysql 数据库中
    :param title:
    :param content:
    :return:
    '''
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
