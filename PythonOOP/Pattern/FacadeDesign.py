#!/usr/bin/python
#coding:utf8
'''
Decorator
'''
import time

star='#'*5
class SystetmOne:
    def start(self):
        print( f'{star} system one start {star}')

    def run(self):
        print( f'{star} system one running {star}')

    def finish(self):
        print( f'{star} system one finish {star}')

class SystetmTwo:
    def start(self):
        print( f'{star} system two start {star}')

    def run(self):
        print( f'{star} system two running {star}')

    def finish(self):
        print( f'{star} system two finish {star}')

class Facade:
    def __init__(self):
        self.sys_one=SystetmOne()
        self.sys_two=SystetmTwo()
        self.all=[i for i in (self.sys_one,self.sys_two)]

    def run(self):
        [(i.start(),i.run(),i.finish()) for i in self.all]

if __name__=='__main__':

    facade=Facade()
    facade.run()