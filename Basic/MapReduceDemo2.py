from functools import reduce

def LowerFirstName(name):
    return name[0:1].upper()+name[1:].lower()

names=['Menglihuan','terry']
for name in names:
    print(LowerFirstName(name))