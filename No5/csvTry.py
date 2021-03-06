from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# csvFile = open("./test.csv", "w+")
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(('number', 'number plus 2', 'number times 2'))
#     for i in range(10):
#         writer.writerow((i, i+2, i*2))
# finally:
#     csvFile.close()

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "lxml")

# 主对比表格是当前页面上的第一个表格
table = bsObj.find("table", {"class": "wikitable"})
rows = table.findAll("tr")

csvFile = open("./editors.csv", "wt", newline='')
writer = csv.writer(csvFile)
try:
    count = 1
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
        print("网页表格中的第%d行已经解析完成"%count)
        count = count + 1
finally:
    csvFile.close()
