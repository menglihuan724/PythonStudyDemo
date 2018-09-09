#!/usr/bin/python
#coding:utf8
'''
Template模板模式
'''

#skeletons

word='l like hsy'
line='*'*10

def iter_elements(getter,action):
    for element in getter():
        action(element)
        print(line)

def revs_elements(getter,action):
    for element in getter()[::-1] :
        action(element)
        print(line)

def get_list():
    return  word.split()

def get_lists():
    return  [list(x) for x in word.split()]

def print_element(e):
    print(e)

def revs_element(e):
    print(e[::-1])

def create_template(skeleton,getter,action):
    def template():
        skeleton(getter , action)
    return template

templates=[create_template(s,g,a)
           for s in (iter_elements,revs_elements)
           for g in (get_list,get_lists)
           for a in (print_element,revs_element)
           ]
print_element((len(templates)))
for template in templates:
    template()