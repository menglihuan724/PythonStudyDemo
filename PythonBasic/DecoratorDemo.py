import time, functools
def metric(fn):

    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        time_start=time.time()
        res=fn(*args,**kwargs)
        time_end=time.time()-time_start
        print('%s usertime %s ms'% (fn.__name__,1000*time_end))
        return res
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print(f,s)
if f == 33 and s == 7986:
    print('success!')
else:
    print('wrong')