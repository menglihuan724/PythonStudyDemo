def odd():
    n=1
    while True:
        n=n+2
        yield n
def myfilter(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=odd()
    while True:
        n=next(it)
        yield n
        it=filter(myfilter(n),it)
for x in primes():
    if x<1000:
        print(x)
    else: break
