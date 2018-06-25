from datetime import datetime
from urllib.parse import urlencode
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import time
import csv
from itertools import product

TOTAL_PAGE_NUMBER = 10  # PAGE_NUMBER: total number of pages，可进行修改

KEYWORDS = ['大数据', 'python', 'java工程师','数据分析'] # 需爬取的关键字可以自己添加或修改

# 爬取主要城市的记录
ADDRESS = ['全国', '北京', '上海', '广州', '深圳',
           '天津', '武汉', '西安', '成都', '大连',
           '长春', '沈阳', '南京', '济南', '青岛',
           '杭州', '苏州', '无锡', '宁波', '重庆',
           '郑州', '长沙', '福州', '厦门', '哈尔滨',
           '石家庄', '合肥', '惠州', '太原', '昆明',
           '烟台', '佛山', '南昌', '贵阳', '南宁']


def download(url):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    response = requests.get(url,headers=headers)

    # print(response.status_code)

    return response.text

def get_content(html):
    date=datetime.now().date()
    date=datetime.strftime(date, "%Y-%m-%d")
    soup=BeautifulSoup(html,'lxml')
    body=soup.body
    data_main=body.find('div',{'class':'newlist_list_content'})
    if data_main:
        tables = data_main.find_all('table')
        for i,table_info in enumerate(tables):
            if i==0:
                continue
            tds = table_info.find('tr').find_all('td')
            zwmc = tds[0].find('a').get_text()  # 职位名称
            zw_link = tds[0].find('a').get('href')  # 职位链接
            fkl = tds[1].find('span').get_text()  # 反馈率
            gsmc = tds[2].find('a').get_text()  # 公司名称
            zwyx = tds[3].get_text()  # 职位月薪
            gzdd = tds[4].get_text()  # 工作地点
            gbsj = tds[5].find('span').get_text()  # 发布日期
            tr_brief = table_info.find('tr', {'class': ' newlist_tr_detail'})
            #brief = tr_brief.find('li', {'class': 'newlist_deatil_last'}).get_text()
            yield{
                #'tds':tds,
                'zwmc':zwmc,
                'zw_link':zw_link,
                'fkl':fkl,
                'gsmc':gsmc,
                'zwyx':zwyx,
                'gzdd':gzdd,
                'gbsj':gbsj,
                #'brief':brief,
                'date':date
            }
def save_tocsv(data, file_name):
     with open (file_name,'w', encoding="gbk", errors='ignore', newline='') as f:
         header=['zwmc','zw_link','fkl','gsmc','zwyx','gzdd','gbsj','date']
         f_csv=csv.DictWriter(f,fieldnames=header)
         f_csv.writerows(data)

def main(args):
    basic_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
    for keyword in KEYWORDS:
        paras = {'jl': args[0],
                 'kw': keyword,
                 'p': args[1]  # 第X页
                 }
    url = basic_url + urlencode(paras)
    html = download(url)
    if html:
        data=get_content(html)
        # for item in data:
        #     print("item是 %s" % type(item))
        save_tocsv(data,'zhilian.csv')
if __name__ == '__main__':
    start=time.time()
    number_list=list(range(TOTAL_PAGE_NUMBER))
    args=product(ADDRESS,number_list)
    pool = Pool()
    pool.map(main, args)
    end = time.time()
    print('Finished, task runs %s seconds.' % (end - start))


