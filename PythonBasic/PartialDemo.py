import  functools
mymax=functools.partial(max,10)
int2 = functools.partial(int, base=2)

#test
print(int2('1001000000',base=16))