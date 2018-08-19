import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

url="https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"

#调用phantomJs
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
drive = webdriver.Chrome(chrome_options=chrome_options)

csv_file=open("gakki.csv", "w", encoding="gb18030", newline="")

writer=csv.writer(csv_file)
writer.writerow(["名字","数量","地址"])

num=1
#解析每页
while (url != 'javascript:void(0)') & (num>0):
    drive.get(url)
    drive.switch_to.frame("contentFrame")
    data=drive.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    #解析每页中的歌单
    for i in range(len(data)):
            nb=data[i].find_element_by_class_name("nb").text
            msk=data[i].find_element_by_css_selector("a.msk")
            writer.writerow([msk.get_attribute("title"), nb, msk.get_attribute("href")])
    url=drive.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")
    --num
csv_file.close()
