import time
def countdown(n):
    while n > 0:
        print n
        n = n-1
        time.sleep(1)
    print 'Blastoff!'

countdown(10)

