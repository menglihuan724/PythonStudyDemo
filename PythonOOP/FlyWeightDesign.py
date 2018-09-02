#!/usr/bin/python
#coding:utf8
'''
Flyweight 享元模式
'''
import weakref


class Music(object):
    _MusicPool=weakref.WeakValueDictionary()

    def __new__(cls, name, author):
        music=Music._MusicPool.get(name+author,None)
        if not music:
            music=object.__new__(cls)
            Music._MusicPool[name+author]=music
            music.name,music.author=name,author
        return  music

    def __repr__(self, *args, **kwargs):
        return f'Music<{self.name,self.author}>'

if __name__ == '__main__':
    m1 = Music('Jay','Jay')
    m2 = Music('Jay','Jay')
    print(m1 == m2)
    print(m1, m2)