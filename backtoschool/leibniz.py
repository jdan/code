from decimal import *
getcontext().prec=15
print '\n'.join(map(str, [sum([(-1)**i/Decimal(2*i+1) for i in range(int(input()))]) for q in range(input())]))

