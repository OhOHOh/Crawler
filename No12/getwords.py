from urllib.request import urlretrieve
from selenium import webdriver
import subprocess, time

driver = webdriver.Firefox(executable_path='/Users/runshen/work/GithubWork/Crawler/No12/geckodriver')
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
# 暂停 2 秒
time.sleep(2)

# 单击图书预览按钮
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

# 暂停 5 秒, 等待页面加载
time.sleep(5)

# 当向右箭头可以点击时，开始翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    #获取已加载的新页面（一次可以加载多个页面，但是重复的页面不能加载到集合中）
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

print('图片收集完毕')

# 用Tesseract处理我们收集的图片URL链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())
