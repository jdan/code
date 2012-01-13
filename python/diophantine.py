from cfrac import *
from sys import argv

print 'Ax - By = 1'
x = int(raw_input('x? '))
y = int(raw_input('y? '))

sol = expand(float(x)/y)
res = compress(sol[:-1])

print '%sx - %sy = 1' % (x, y)
print 'x = %s, y = %s' % (res[1], res[0])

if len(argv) == 2:
    if int(argv[1]) == 1:
        print 'Error: %s' % (x * res[1] - y * res[0] - 1)
