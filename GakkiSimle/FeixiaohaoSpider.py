import csv
import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import  BeautifulSoup
import json
import pymongo
import re

#chrome配置及地址
num=1
url=f'https://www.feixiaohao.com/notice/list_{num}.html'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver2 = webdriver.Chrome(chrome_options=chrome_options)

#写入csv文件
csv_file=open("gakki.csv", "w", encoding="gb18030", newline="")
writer=csv.writer(csv_file)
writer.writerow(["标题","时间","内容url","内容"])
while num<=337:
    #点击更多按钮
    print(url)
    driver.get(url)
    notice_list=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul').find_elements_by_tag_name('li')
    #解析每页中的歌单
    for li in notice_list:
        the_one=li.find_element_by_class_name("tit")
        #title
        title=the_one.get_attribute('title')
        #url
        content_url=the_one.get_attribute('href')
        #time
        time=the_one.find_element_by_class_name('time').text
        #content
        content=''
        if not re.search('feixiaohao', content_url) is None:
            driver2.get(content_url)
            content=driver2.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div').text
        else:
            content='第三方内容,不爬取'

        #print (f'title:{title},time:{time},url:{url},content:{content}')

        writer.writerow([title, time, content_url, content])
    num+=1
    url=f'https://www.feixiaohao.com/notice/list_{num}.html'

# def loop(num):
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)