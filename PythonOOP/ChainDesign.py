#!/usr/bin/python
#coding:utf8

"""
Chain 责任链模式
"""
from astroid.protocols import _augmented_name


class Handler():
    def next(self,hanler):
        self.next=hanler
class ChainOne(Handler):
    def handle(self,req):
        if req>=0 and req<=10:
            print (f'chain one deal with req{req}')
        else:
            self.next.handle(req)

class ChainTwo(Handler):
    def handle(self,req):
        if req>10 and req<=50:
            print (f'chain two deal with req{req}')
        else:
            self.next.handle(req)

class ChainThree(Handler):
    def handle(self,req):
        if req>50 and req<=100:
            print (f'chain three deal with req:{req}')
        else:
            print('no handler can deal with this req:{req}')

if __name__=='__main__':
    chainOne=ChainOne()
    chainTwo=ChainTwo()
    chainThree=ChainThree()
    chainOne.next(chainTwo)
    chainTwo.next(chainThree)

    reqs=range(0,101)
    for i in reqs:
        chainOne.handle(i)