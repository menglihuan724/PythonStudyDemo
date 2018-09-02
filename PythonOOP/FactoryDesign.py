#coding:utf8
'''
工厂模式
'''

class chineseGetter:
    def __init__(self):
        self.trans=dict(dog=u'狗',cat=u'猫')

    def get(self,msgid):
        try:
            self.trans[msgid]
        except KeyError:
            return str(msgid)
class englishGetter:
    def get(self,msgid):
        return str(msgid)

def get_factory(language='english'):
    languages=dict(english=englishGetter,chinese=chineseGetter)
    return languages[language]()

if __name__ == '__main__':
    e,c=get_factory('english'),get_factory('chinese')
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid),c.get(msgid))