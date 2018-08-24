#wrong closure
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print("wrong closure")
print(f1())
print(f2())
print(f3())
#correct closure
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fn=[]
    for i in range(1,4):
       fn.append(f(i))
    return fn

f4,f5,f6=count2()
print("correct closure")
print(f4(),f5(),f6())

def createCounter():
    data = [0]
    def counter():
        data[0] += 1
        return data[0]
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA(),counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')