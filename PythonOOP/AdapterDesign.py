#coding:utf8
'''
Adapter
'''

import  os

class Man():
    def __init__(self,name):
          self.name=name
          self.gender="man"
    def yell(self):
        return "oh,oh,oh"
class Woman():
    def __init__(self,name):
        self.name=name
        self.gender="woman"
    def yell(self):
        return "yes baby,oh,yeah"
class PeopleAdapter:
    def __getattr__(self,attr):
          return getattr(self.obj,attr)

    def __init__(self, obj, adapted_methods):
        self.obj=obj
        self.__dict__.update(adapted_methods)

def main():
    objects=[]
    terry=Man("terry")
    objects.append(PeopleAdapter(terry,dict(yell=terry.yell)))
    hsy=Woman("hsy")
    objects.append(PeopleAdapter(hsy,dict(yell=hsy.yell)))

    for people in objects:
        print("a people name's", people.name, "yell", people.yell())

if __name__== "__main__":
    main()