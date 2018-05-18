from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def StrToInt(s):
    def fn(x,y):
        return x*10+y
    def charToNum(s):
        return DIGITS[s]
    return reduce(fn,map(charToNum,s))
x=StrToInt('5');
print(x)

