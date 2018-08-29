#!/usr/bin/python
#coding:utf8
'''
Bridge
'''

class DrawingApiOne(object):
    def draw_circle(self,x,y,radius):
        print("ApiOne draw at x:{},y:{},radius:{}".format(x,y,radius))


class DrawingApiTwo(object):
    def draw_circle(self,x,y,radius):
        print("ApiTwo draw at x:{},y:{},radius:{}".format(x,y,radius))

class CircleSharp(object):
    def __init__(self,x,y,radius,api):
        self.x=x
        self.y=y
        self.radius=radius
        self.draw_api=api
    def draw(self):
        self.draw_api.draw_circle(self.x,self.y,self.radius)
    def scale(self,pct):
        self.radius*=pct
def main():
    shapes=(CircleSharp(1,2,3,DrawingApiOne()),CircleSharp(2,3,4,DrawingApiTwo()))
    for shape in shapes:
        shape.scale(10)
        shape.draw()

if __name__ == '__main__':
    main()


