#!/usr/bin/python
#coding:utf8
'''
Prototype
'''
import copy


class Prototype:

    def __init__(self):
        self.objects={}
    def regs_object(self,name,object):
        self.objects[name]=object
    def del_object(self,name):
        del self.objects[name]
    def clone(self,name,**attr):
        obj=copy.deepcopy(self.objects.get(name))
        obj.__dict__.update(attr)
        return obj

def main():
    class Test:
        def __str__(self):
            return 'im test'
    test=Test()
    prototype=Prototype()
    prototype.regs_object('test',test)
    b=prototype.clone('test',a=7,b=2,c=4)
    print(test)
    print(b.a, b.b, b.c)


if __name__ == '__main__':
     main()
