import time,threading
bal=0
lock=threading.Lock()
def change(n):
    global bal
    bal=bal+n
    bal=bal-n
def runWithOutLock(n):
    for i in range(1000000):
        change(n)
def runWithLock(n):
    for i in range(1999998):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()
#test
t1=threading.Thread(target=runWithLock,args=(24,))
t2=threading.Thread(target=runWithLock,args=(25,))
t1.start()
t2.start()
t1.join()
t2.join()
print(bal)