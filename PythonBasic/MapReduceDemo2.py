from functools import reduce

def LowerFirstName(name):
    return name[0:1].upper()+name[1:].lower()

def prod(L):
    def plus(x,y):
        return x*y
    return reduce(plus,L)

names=['Menglihuan','terry']
for name in names:
    print(LowerFirstName(name))
total=prod(list(range(1,20)))
print(total)