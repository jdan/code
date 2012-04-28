#!/usr/bin/python

from math import log10, floor

f = file('C-large.in')
n = int(f.readline())

for i in range(n):
    line = f.readline().split()
    A = int(line[0])
    B = int(line[1])
    
    res = 0
    
    for k in range(A, B+1):
        d = int(floor(log10(k)))
        cyc = k
        found = []
        for h in range(d):
            cyc = cyc / 10 + (cyc % 10) * (10 ** d)
            if cyc > k and cyc <= B and cyc not in found:
                found.append(cyc)
                res += 1
    
    print 'Case #%s: %s' % (i+1, res)