#!/usr/bin/python
#coding:utf8

"""
    Builder 建造模式
"""

class Director(object):
    def __init__(self):
        self.builder=None
    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()
    def get_building(self):
        return  self.builder.building


class Building(object):
    def __init__(self):
        self.floor=None
        self.size=None

    def __repr__(self) :
        return f'Floor:{self.floor},Size:{self.size}'


class Builder(object):
    def __init__(self):
        self.building=None
    def new_building(self):
        self.building=Building()

class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor='one'
    def build_size(self):
        self.building.size='small'

class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor='More than one'
    def build_size(self):
        self.building.size='big'

if __name__=='__main__':
    director=Director()
    director.builder=BuilderHouse()
    director.construct_building()
    building=director.get_building()
    print(building)

    director.builder=BuilderFlat()
    director.construct_building()
    building=director.get_building()
    print(building)
