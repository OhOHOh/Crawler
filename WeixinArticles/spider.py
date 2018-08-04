from urllib.parse import urlencode

import re
import requests
from requests.exceptions import ConnectionError
from config import *
from pyquery import PyQuery as pq


base_url = 'http://weixin.sogou.com/weixin?'
headers = {
        'cookies': 'IPLOC=CN3100; SUV=000D111E6FBB318359C8BE86BA771808; SUID=E10888755218910A000000005B5FC0B8; SNUID=33DB5BA7D2D6A1930107F3C5D30E662B; ABTEST=0|1533001944|v1; weixinIndexVisited=1; JSESSIONID=aaalDPdRsj9b2-zSmJHsw; sct=2; ppinf=5|1533110038|1534319638|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA; pprdig=JzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew; sgid=02-34274603-AVthZxaUsZp4ACtJ9b5kOia8; ppmdig=1533110038000000f06734556f3a35c65309af2683c0784b',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
    }

proxy = None

def get_proxy(pCount=1):
    if pCount >= 10:
        print('无可用 proxy')
        return None
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return get_proxy(pCount)
    except ConnectionError:
        pCount += 1
        return get_proxy(pCount)

def get_index_html(url, vCount=1):
    print("Crawling url: ", url)
    # print("Trying counts: ", count)
    if vCount >= 5:
        print('Failed visiting {0} too many times'.format(url))
    global proxy
    try:
        if proxy:
            print('Using proxy: ', proxy)
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, headers=headers, allow_redirects=False, proxies=proxies)
        else:
            response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            # print('200')
            return response.text
        if response.status_code == 302:
            # ip 被封, 换爬虫
            print('302, 需要更换新的爬虫')
            proxy = get_proxy()
            return get_index_html(url, vCount)
    except ConnectionError:
        vCount += 1
        get_index_html(url, vCount)

def get_index(keyword, pageIndex):
    params = {
        'query': keyword,
        'type': 2,
        'page': pageIndex
    }
    url = base_url + urlencode(params)
    html = get_index_html(url)
    if html:
        print('Success 爬取 {0} 页面成功！'.format(url))
        return html
    else:
        print('Fail 爬取 {0} 页面失败！'.format(url))
        return None

def parse_index(html):
    """
    从 html 代码中提取出 每一个微信文章的地址, 一个 index 页有 10 篇微信文章
    :param html: 从 get_index() 中获取 index 页的 html 代码, 可能为空
    :return: list(yield) 存微信文章的地址
    """
    if html:
        url_pattern = re.compile('<a.*?href="(.*?)".*?data-share')
        result = re.findall(url_pattern, html)
        if result:
            for item in result:
                yield item.replace('amp;', '')
        else:
            return None
    else: return None

def get_detail(url):
    """
    从 url 中获取 微信文章的 html 代码
    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    doc = pq(html)
    title = doc('.rich_media_title').text()
    content = doc('.rich_media_content ').text()
    date = doc('#publish_time').text()
    nickName = doc('.rich_media_meta_list .rich_media_meta_nickname').text()
    wechatId = doc('#js_profile_qrcode > div > strong').text()
    return {
        'title': title,
        'content': content,
        'date': date,
        'nickName': nickName,
        'wechatId': wechatId
    }



if __name__ == '__main__':
    # print(get_index(1))
    for i in range(1, 101):
        html = get_index(KEY_WORD, i)
        article_urls = parse_index(html)
        if article_urls:
            for url in article_urls:
                article_html = get_detail(url)
                dict = parse_detail(article_html)
                print(dict)
