class Student():
    count=0
    __slots__ = ('__name','grade','height')
    def __init__(self,name,grade):
        self.__name=name
        self.grade=grade
        Student.count+=1
    def printAll(self):
        print('name:%s \n grade:%s'% (self.__name,self.grade))
    def get_name(self):
        return self.__name
#test
terry=Student('menglihuan',78)
jorge=Student('jorge',99)
terry.printAll()
print(terry.get_name())
print(Student.count)
terry.height=162
terry.weight=33
#print(terry._Student_name)