#!/usr/bin/python
#coding:utf8

"""
Composite 组合模式
"""

class Component:

    def __init__(self,strName):
        self.m_strName=strName

    def add(self,com):
        pass
    def display(sele,depth):
        pass

class Composite(Component):
    def __init__(self, strName):
        self.m_strName = strName
        self.c = []
    def add(self, com):
        self.c.append(com)

    def display(self, depth):
        strTemp='-'*depth
        strTemp=strTemp+self.m_strName
        print(strTemp)
        for com in self.c:
            com.display(depth+2)
class Leaf(Component):
    def add(self, com):
        print('no add for leaf')

    def display(self, depth):
        strTemp='-'*depth
        strTemp=strTemp+self.m_strName
        print(strTemp)

if __name__=='__main__':
    com=Composite('parent')
    com.add(Leaf('child1'))
    com.add(Leaf('child2'))
    com2=Composite('parent2')
    com2.add(Leaf('child3'))
    com.add(com2)
    com.display(1)

