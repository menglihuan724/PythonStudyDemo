#!/usr/bin/python
#coding:utf8
'''
Singleton 单例模式
'''

class Singleton(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            # org=super(Singleton,cls)
            cls._instance=super().__new__(cls)
        return cls._instance

class SingletonTest(Singleton):
    def __init__(self,name) :
        self.name=name

    def __str__(self) :
        return  self.name

if __name__=='__main__':
    a=SingletonTest('terry')
    print(id(a),a)
    b=SingletonTest('hsy')
    print(id(b),b)
    print(id(a),a)


