from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, csv

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, 'lxml')

# table = bsObj.find("table", {"class": "wikitable sortable jquery-tablesorter"})

table = bsObj.find("table", {"class": "wikitable"})
# print(table)
rows = table.findAll("tr")
# print(rows)

csvFile = open("./editors.csv", "wt", newline='')
writer = csv.writer(csvFile)

try:
    count = 1
    for row in rows:
        csvRow = []
        for cell in row.findAll(["th", "td"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
        print("网页表格中的第%d行已经解析完成"%count)
        count = count + 1
finally:
    csvFile.close()

