from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    '''
    有限制条件地返回 articleUrl 中的链接(Links)
    :param articleUrl:
    :return:
    '''
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistory(pageUrl):
    # 编辑历史页面的 URL 格式是
    #  http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is " + historyUrl)  # 验证一波
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "lxml")
    # 找出class属性是"mw-anonuserlink"的链接
    # 它们用IP地址代替用户名
    ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())

    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_name')


links = getLinks("/wiki/Python_(programming_language)")

# for link in links:
#     print(link.attrs['href'])

while (len(links) > 0) :
    for link in links:
        print("-------------------")
        historyIPs = getHistory(link.attrs['href'])
        for historyIP in historyIPs:
            #print(historyIP)
            print(getCountry(historyIP))

    # newLinks = links[random.randint(0, len(links)-1)].attrs["href"]
    # links = getLinks(newLinks)

