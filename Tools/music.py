#!/usr/bin/env python
# encoding: utf-8

"""
@author: sergiojune
@contact: 2217532592@qq.com
@site: 
@software: PyCharm
@file: music.py
@time: 2018/8/8 16:15
"""
import requests
import random, math
from Crypto.Cipher import AES
import base64
import codecs
import os
"""
获取歌曲地址：https://music.163.com/weapi/song/enhance/player/url?csrf_token=b15a182044ebb9acfa5e4ade219a064c
"""


class Spider(object):
    def __init__(self):
        self.headers = {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
                 'Cookie':'_iuqxldmzr_=32; _ntes_nnid=beb14e9fd6b7bda48d84539e6aea158e,1536228039665; _ntes_nuid=beb14e9fd6b7bda48d84539e6aea158e; __utmc=94650624; WM_TID=ORCl30z5q9ZmbgMeYltBrrhGJLH0R0nC; playerid=19729879; __utma=94650624.1292913758.1536228041.1536228041.1536228041.1; __utmz=94650624.1536228041.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=S5gViyNVs14K%2BZoVerGK69gLlmtnH5NqzyHcCUY%2BiWm2ZaHATeI1gfsEnK%2BQ1jyP%2FROzbzDV0AyJHR4YQfBetXSRipyrYCFn%2BNdA%2FA8Mv80riS3cuMVJi%2BAFgCpXTiHBNHE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8cd75df3bbb8d3e466f491ae83ee41abb89bafca4ef58d85a2bc64f29884aac92af0fea7c3b92afba6feb2f874edeab8d8ec3af3998495f33ef7b4c0d0d565b2979b99f77ae99fbfb7e74bb8f59ba8e95096998883c259a7e9fa97db4b918b8892e83e899dac97d47ba588fed3c24db6f1b993f54689e99babfb44818a8f90aa5df494c0dafb4dbce8acaccd70939ba0b6d94583b6f889cd53a69ab696b23fba97a8b0f472aabc9ea8ee37e2a3; JSESSIONID-WYYY=zfQFEmmjws8nyX8KXTF4I6wdhWIuKXnyGJhx%2FN88kj37jyviGJGtRtV%2FgrsKu8AHTFb6F%2FSjocaCnbkNKyqN%2F4%2FO%2FvxkGjopumxxS%2FmASXFhkPH6rB37w7%2FQhQVQlKqKCh6g9bnPl38Z2eo86gSYAJBSa%5CpxCWrYbvD6WbZ%5ChOabpeRE%3A1536229839571'

        }

    def __get_songs(self, name):
        d = '{"hlpretag":"<span class=\\"s-fc7\\">","hlposttag":"</span>","s":"%s","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}' % name
        wyy = WangYiYun(d)    # 要搜索的歌曲名在这里
        data = wyy.get_data()
        url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        response = requests.post(url, data=data, headers=self.headers).json()
        return response['result']

    def __get_mp3(self, id):
        d = '{"ids":"[%s]","br":320000,"csrf_token":""}' % id
        wyy = WangYiYun(d)
        data = wyy.get_data()
        url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
        response = requests.post(url, data=data, headers=self.headers).json()
        print(response)
        return response['data'][0]['url']

    def __download_mp3(self, url, filename):
        """下载mp3"""
        abspath = os.path.abspath('.')  # 获取绝对路径
        os.chdir(abspath)
        response = requests.get(url, headers=self.headers).content
        path = os.path.join(abspath, filename)
        with open(filename + '.mp3', 'wb') as f:
            f.write(response)
            print('下载完毕,可以在%s   路径下查看' % path + '.mp3')

    def __print_info(self, songs):
        """打印歌曲需要下载的歌曲信息"""
        songs_list = []
        for num, song in enumerate(songs):
            print(num, '歌曲名字：', song['name'], '作者：', song['ar'][0]['name'])
            songs_list.append((song['name'], song['id']))
        return songs_list

    def run(self):
        while True:
            name = input('请输入你需要下载的歌曲：')
            songs = self.__get_songs(name)
            if songs['songCount'] == 0:
                print('没有搜到此歌曲，请换个关键字')
            else:
                songs = self.__print_info(songs['songs'])
                num = input('请输入需要下载的歌曲，输入左边对应数字即可')
                url = self.__get_mp3(songs[int(num)][1])
                if not url:
                    print('歌曲需要收费，下载失败')
                else:
                    filename = songs[int(num)][0]
                    self.__download_mp3(url, filename)
                flag = input('如需继续可以按任意键进行搜歌，否则按0结束程序')
                if flag == '0':
                    break
        print('程序结束！')


class WangYiYun(object):
    def __init__(self, d):
        self.d = d
        self.e = '010001'
        self.f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5a" \
                 "a76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46be" \
                 "e255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.g = "0CoJUm6Qyw8W8jud"
        self.random_text = self.get_random_str()

    def get_random_str(self):
        """js中的a函数"""
        str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        res = ''
        for x in range(16):
            index = math.floor(random.random() * len(str))
            res += str[index]
        return res

    def aes_encrypt(self, text, key):
        iv = '0102030405060708'  # 偏移量
        pad = 16 - len(text.encode()) % 16  # 使加密信息的长度为16的倍数，要不会报下面的错
        # 长度是16的倍数还会报错，不能包含中文，要对他进行unicode编码
        text = text + pad * chr(pad)  # Input strings must be a multiple of 16 in length
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        msg = base64.b64encode(encryptor.encrypt(text))  # 最后还需要使用base64进行加密
        return msg

    def rsa_encrypt(self, value, text, modulus):
        '''进行rsa加密'''
        text = text[::-1]
        rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(value, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)

    def get_data(self):
        # 这个参数加密两次
        params = self.aes_encrypt(self.d, self.g)
        params = self.aes_encrypt(params.decode('utf-8'), self.random_text)
        enc_sec_key = self.rsa_encrypt(self.e, self.random_text, self.f)
        return {
            'params': params,
            'encSecKey': enc_sec_key
        }


def main():
    spider = Spider()
    spider.run()


if __name__ == '__main__':
    main()
