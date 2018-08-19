from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import  BeautifulSoup
import json
import pymongo
import argparse

#mongo链接
myclient = pymongo.MongoClient("mongodb:/")
mydb = myclient["gakki"]
mycol = mydb["card"]

#chrome驱动
url="https://m.weibo.cn/api/container/getIndex?containerid=1076031882811994&page="
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

#需要抓取的页数
def getPages(num):
    all_cards=[]
    while num>0:
        driver.get(url+str(num))
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        res = json.loads(soup.select('pre')[0].string)
        cards_list=res['data']['cards']
        for card in cards_list:
         all_cards.append(card)
        num-=1
    ids=mycol.insert_many(all_cards)
    print(ids.inserted_ids)

def main():
    parser = argparse.ArgumentParser(description='Welcome to GakkisimleSpider')
    parser.add_argument('-n', metavar='num', dest='num',
                        help='需要下载的页数')
    args = parser.parse_args()
    if args.num:
        getPages(num=int(args.num))
    else:
        getPages(num=1)

if __name__ == '__main__':
    main()
