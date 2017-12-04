from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    unix_socket='/var/run/mysqld/mysqld.sock',
    user='root',
    passwd='123',
    db='wikipedia',
    charset='utf8'
)
cur = conn.cursor()

def insertPageIfNotExists(url):
    '''
    如果在 pages 表中不存在 url, 那么就插入到表中, 最后都返回当前 url 在表 pages 中对应的 id
    :param url:
    :return:
    '''
    cur.execute("SELECT * FROM pages WHERE url=%s", (url))
    if cur.rowcount == 0:
        # pages 表中不存在 url
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId=%s AND toPageId=%s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)", (int(fromPageId), int(toPageId)))
        conn.commit()

pages = set()
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs["href"]))
        if link.attrs["href"] not in pages:
            # 遇到一个新页面,加入集合并搜索里面的词条链接
            newPage = link.attrs["href"]
            print(newPage)
            pages.add(newPage)
            getLinks(newPage, recursionLevel+1)


getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
