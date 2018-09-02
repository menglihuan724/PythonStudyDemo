#!/usr/bin/python
#coding:utf8
'''
Proxy 代理模式
'''
import time


class RemotelyMethod:
    def excute(self,args):
        print(args)
        return 'success'
    def error(self):
        return 'error'
class Proxy:
    def __init__(self):
        self.netWork='Normal'
        self.method=None

    def excute(self,args):
        print('proxy excute romotely method')
        if self.netWork=='Normal':
            self.method=RemotelyMethod()
            time.sleep(2)
            res=self.method.excute(args)
        else:
            time.sleep(2)
            res=self.method.error()

        print(res)

if __name__ == '__main__':
    p = Proxy()
    p.excute("pls do something")
    p.netWork = 'NetWork Wrong'
    p.excute("pls do something")