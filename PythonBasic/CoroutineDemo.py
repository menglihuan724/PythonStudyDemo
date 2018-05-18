def consumer():
    r=''
    while True:
        n = yield r
        if not n:
            return
        print('consumer %s..'% n)
def provider(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('provider %s'% n)
        r=c.send(n)
        print('consumer %s..'% r)
    c.close()
c=consumer()
provider(c)
