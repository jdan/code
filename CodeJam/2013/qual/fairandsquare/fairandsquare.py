#!/usr/bin/python

from sys import argv
from math import sqrt

def main():
    f = file(argv[1])
    n = int(f.readline())

    for i in range(n):
        a, b = map(int, f.readline()[:-1].split(' '))

        total = 0
        for q in range(a, b+1):
            if is_fair_and_square(q):
                total += 1

        print 'Case #%s: %s' % (i + 1, total)


def is_fair_and_square(n):
    if sqrt(n) == int(sqrt(n)):
        return is_palindrone(n) and is_palindrone(int(sqrt(n)))

def is_palindrone(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    main()
