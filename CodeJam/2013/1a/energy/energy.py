#!/usr/bin/python

from sys import argv
from math import sqrt

def energy(max_e, e, gain, activities):
    if activities == []:
        return 0
    else:
        return max([i * activities[0] + energy(max_e, min(max_e, e - i + gain), gain, activities[1:]) for i in range(e+1)])

def main():
    f = file(argv[1])
    n = int(f.readline())

    for i in range(n):
        e, r, _ = map(int, f.readline()[:-1].split(' '))

        gains = map(int, f.readline()[:-1].split(' '))

        print 'Case #%s: %s' % (i + 1, energy(e, e, r, gains))

if __name__ == '__main__':
    main()
