from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re, string

def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', ' ', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'UTF-8')
    input = input.decode("ascii", "ignore")
    input = input.upper()
    cleanInput = []
    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation)   # 获取 python 所有的标点符号
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    '''
    这里首先把内容中的换行符(或者多个换行符)替换成空格,然后把连续的多个空格替换成一个空格,确保所有单词之间只有一个空格。
    最后,把内容转换成 UTF-8 格式以消除转义字符。
    :param input: string
    :param n:
    :return:
    '''
    # input = re.sub('\n+', " ", input)
    # input = re.sub(' +', " ", input)
    # input = bytes(input, "UTF-8")
    # input = input.decode("ascii", "ignore")
    # print(input)
    # input = input.split(' ')
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i: i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "lxml")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams1 = ngrams(content, 2)
#ngrams1  is something like this [['This', 'article'], ['article', 'is'], ['is', 'about'], ['about', 'the'], ['the', 'programming'], ['programming', 'language'],

ngrams = {}
for i in ngrams1:
    j = str(i)   # the key of ngrams should not be a list
    ngrams[j] = ngrams.get(j, 0) + 1
    # ngrams.get(j, 0) means return a value for the given key j. If key j is not available, then returns default value 0.
    # when key j appear again, ngrams[j] = ngrams[j]+1

ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))

# print(content)
# print(type(content))
# print('\n\n\n')
# print(ngrams1)

print(ngrams)
print("2-grams count is:"+str(len(ngrams)))
