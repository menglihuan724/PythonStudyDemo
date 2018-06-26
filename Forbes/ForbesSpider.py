# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup
import csv


def download(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    reponse = requests.get(url, headers=headers)
    return reponse.text


def get_content_first_page(html, country='China'):
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    label_div = body.find('div', {'class': 'content post'})
    tables = label_div.find_all('table')
    trs = tables[0].find_all('tr')
    row_title = [td.text for td in trs[0].find_all('td')]
    row_title.insert(2, 'country')
    data_list = []
    data_list.append(row_title)
    for i, tr in enumerate(trs):
        if i == 0:
            continue
        tds = tr.find_all('td')
        # 公司排名
        row = [item.text.strip() for item in tds]
        row.insert(2, country)
        data_list.append(row)
    return data_list


def get_country_info(html):
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    label_div = body.find('div', {'class': 'content post'})
    tables = label_div.find_all('table')
    label_a = tables[1].find_all('a')
    country_names = [item.text for item in label_a]
    page_urls = [item.get('href') for item in label_a]
    country_info = list(zip(country_names, page_urls))
    return country_info


def get_content_other_country(html, country_name):
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    label_div = body.find('div', {'class': 'content post'})
    tables = label_div.find_all('table')
    trs = tables[0].find_all('tr')
    row_title = [td.text for td in trs[0].find_all('td')]
    row_title.insert(2, 'country')
    data_list = []
    data_list.append(row_title)
    for i, tr in enumerate(trs):
        if i == 0:
            continue
        tds = tr.find_all('td')
        # 公司排名
        row = [item.text.strip() for item in tds]
        row.insert(2, country_name)
        data_list.append(row)
    return data_list


def save_data_to_csv_file(data, file_name):
    print(data)
    # 保存数据到csv文件中
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


def get_forbes_global_year_2013():
    url = 'http://www.economywatch.com/companies/forbes-list/china.html'
    html = download(url)
    data_first_page = get_content_first_page(html)
    print('saving data...', 'china')
    save_data_to_csv_file(data_first_page, 'forbes_2013.csv')
    country_info = get_country_info(html)
    for x, item in enumerate(country_info):
        if(x>=1):
            break
        country_name = item[0]
        country_url = item[1]
        if country_name == 'China':
            continue
        html = download(country_url)
        data_other_country = get_content_other_country(html, country_name)
        print('saving data ...', country_name)
        save_data_to_csv_file(data_other_country, 'forbes_2013.csv')


if __name__ == '__main__':

    # get data from Forbes Global 2000 in Year 2013
    get_forbes_global_year_2013()
    #print( get_content_first_page(download('http://www.economywatch.com/companies/forbes-list/china.html')))