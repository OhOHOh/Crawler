from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, string, operator

def cleanInput(input):
    input = re.sub("\n+" ," ", input)
    input = re.sub("\[[0-9]*\]", " ", input)
    input = re.sub(" +", " ", input)
    input = bytes(input, 'UTF-8')
    input = input.decode("ascii", "ignore")
    input = input.upper()
    input = input.split(" ")

    cleanInput = []

    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a') or (item.lower() == 'i'):
            cleanInput.append(item)

    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramsTemp = " ".join(input[i:i+n])
        if ngramsTemp not in output:
            output[ngramsTemp] = 0
        output[ngramsTemp] += 1
    return output

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
print(sortedNGrams)
