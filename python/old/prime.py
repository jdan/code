from math import sqrt

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3,sqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def isPrime2(n):
    return ((n - 1) % 6 == 0 or (n + 1) % 6 == 0) and n % 5 <> 0 and n % 7 <> 0 \
           and n % 11 <> 0 and n % 13 <> 0

i = 10

while True:
    if isPrime(i) <> isPrime2(i):
        print 'There is a problem with ', i
    i += 1
