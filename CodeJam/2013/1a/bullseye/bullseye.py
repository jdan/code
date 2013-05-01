#!/usr/bin/python

import decimal

decimal.getcontext().prec = 60

from sys import argv
from math import sqrt, floor

def main():
    f = file(argv[1])
    n = int(f.readline())

    for i in range(n):
        r, t = map(int, f.readline()[:-1].split(' '))

        m = int(((1 - 2*r) + decimal.Decimal((2*r - 1)**2 + 8*t).sqrt()) / decimal.Decimal(4.0))

        print 'Case #%s: %s' % (i + 1, m)

if __name__ == '__main__':
    main()
