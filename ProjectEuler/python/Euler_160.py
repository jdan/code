#!/usr/bin/python

def factorial(n):
    t = 1
    for i in range(1, n+1):
        t *= i
    return t
    
for k in range(1, 51):
    print '%s: %s' % (k, factorial(k))