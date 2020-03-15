# -*- coding=utf-8 -*-
'''
2020/3/15
男人帮爬取
'''
import threading
from queue import Queue

import requests
import csv
from bs4 import BeautifulSoup


def new_task(i, headers, factory, q):
    x = 1
    while x < 100:
        factory_name = factory['href']
        print(f'片商{factory_name} 页数:{x}')
        num = x
        if x == 1:
            num = ""
        factory_url = host + factory_name + f'index{num}.html'
        resp2 = session.get(url, headers=headers)
        if resp2.status_code == 404:
            continue
        soup2 = BeautifulSoup(resp.text, "html.parser")
        for j, content in enumerate(soup2.find_all(class_="book-layout")):
            # if j > 1:
            #     break
            content_url = host + content['href']
            img = content.img
            video_num = img['alt']
            video_img = img['data-echo']
            # content_string = content.div.p.string
            row = [i, factory_name, factory_url, content_url, video_num, video_img]
            q.put(row)
        x = x + 1


session = requests.session()
session.keep_alive = True
host = "http://nanrenvip.city/"
url = host + "time.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Referer": "http://nanrenvip.city/olds.html",
    "Host": "nanrenvip.city",
    "Connection": "keep-alive"
}

resp = session.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")
q = Queue()
Thread_list = []
file = []
for i, factory in enumerate(soup.find_all(class_="module-field-cell")):
    t = threading.Thread(target=new_task, args=(i, headers, factory, q))
    t.start()
    Thread_list.append(t)
for i in Thread_list:
    i.join()
while not q.empty():
    row = q.get()
    file.append(row)

with open("nanrenvip.csv", 'a', errors='ignore', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(file)
