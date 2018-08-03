from urllib.parse import urlencode
import os
import pymongo
from hashlib import md5
from requests.exceptions import RequestException, ConnectionError
import requests, re, json
from bs4 import BeautifulSoup
from pprint import pprint
from config import *
from multiprocessing import Pool


client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]
page_detail_number = 0

def get_page_index(offset, keyword):
    """
    获取 20 行的美图图集, 返回含有 20 行美图的图集地址的 JSON 数据
    :param offset: 偏移量, int 0, 20, 40, 60, ...
    :param keyword: string '街拍'
    :return: 返回通过 Ajax 请求而获得的 数据, 类型是 json 格式的 String
    """
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery'
    }
    try:
        url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
        # print(url)
        response = requests.get(url)
        if response.status_code == 200:
            # print('response.text的属性: {0}'.format(type(response.text)))
            return response.text
        else:
            return response.status_code
    except RequestException:
        print('get_page_index() RequestException, 请求索引页出错')
        return None

def parse_page_index(html):
    '''
    对含有 20 行美图的图集地址的 JSON 数据进行解析, 提取出 图集地址
    :param html: 输入的 JSON 格式的 String
    :return: list, 内容是每行图集对应的 url
    '''
    try:
        html = json.loads(html)
        if html and 'data' in html.keys():
            items = html['data'] #<class 'list'> 其中每项元素 item 都是 <class 'dict'>
            for item in items:
                yield item['article_url']
    except:
        print("parse_page_index() 解析失败")

def get_page_detail(url):
    '''
    进入图集的具体页面
    :param url: 图集的 url
    :return: 图集页面的 web 代码 String
    '''
    try:
        global page_detail_number
        headers = {'user-agent':
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_detail_number += 1
            print('现在进入第{0}个图集'.format(page_detail_number))
            return response.text
        else:
            return response.status_code
    except RequestException:
        print('get_page_detail() RequestException, 请求索引页出错')
        return None

def parse_page_detail(html, url):
    '''
    解析页面代码, 获取该图集下的所有图片的地址
    :param html:
    :param url: 图集的地址
    :return: dict, 标题 + 图片的下载地址(list)
    '''
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    # images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)', re.S) # 1
    images_pattern = re.compile('gallery: JSON.parse\((.*?)\)', re.S)
    result = re.search(images_pattern, html)
    # print(result.group(1))
    # print(type(result.group(1)))  # <class 'str'>
    if result:
        # data = json.loads(result.group(1).replace('\\', '')) # 1
        data = json.loads(json.loads(result.group(1)))
        # print('type(data):  {0}'.format(type(data)))
        # pprint(data)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images_url = [item.get('url') for item in sub_images]
            # for url in images_url:
            #     download_image(url)
            return {
                'title': title,
                'url': url,
                'images_url': images_url
            }

def get_parse_page_detail(url):
    try:
        headers = {'user-agent':
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        response=requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.select('title')[0].get_text()
        # response.encoding=response.apparent_encoding
        images_pattern = re.compile('gallery: JSON.parse\((.*?)\)' , re.S)
        result = re.search(images_pattern, response.text)
        # print (result.group(1))
        if result:
            group = result.group(1)
            data = json.loads(json.loads(group))
            # print(type(s))
            # print(s.get('sub_images'))
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images_url = [item.get('url') for item in sub_images]
                return {
                    'title': title,
                    'url': url,
                    'images_url': images_url
                }
    except:
        print("请求详情页错误")

def save_image(content):
    file_path = '{0}/pictures/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def download_image(url):
    '''
    下载 图片
    :param url: 图片地址 str
    :return:
    '''
    print('downloading: ' + url)
    try:
        headers = {'user-agent':
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except ConnectionError:
        return None

def save_to_mongo(result):
    """
    保存到 mongodb 中
    :param result: dict
    :return:
    """
    if db[MONGO_TABLE].insert(result):
        print('Successfully Saved to Mongo', result)
        return True
    return False



def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html): # 得到 图集 的 url
        html = get_page_detail(url)
        if html:
            dict = parse_page_detail(html, url)
            if dict: save_to_mongo(dict)
        # print(get_parse_page_detail(url))


if __name__ == '__main__':
    # for i in range(GROUP_START, GROUP_END + 1):
    #     main(i*20)
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    pool = Pool()
    pool.map(main, groups)
