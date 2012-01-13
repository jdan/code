from sys import argv
from math import sqrt

a = map(int, argv[1].split(','))

def nested(r):
    if len(r) > 1:
        return r[0] * sqrt(1 + nested(r[1:]))
    else:
        return r[0]
        
print nested(a)
