from math import *

def drawstar(n, outer, inner, x = 0, y = 0, f = 'output.path'):
    fout = open(f, 'w')
    a = 2*pi / (2 * n)
    for i in range(2*n + 1):
        nx = cos(i * a)
        ny = sin(i * a)
        
        if i % 2 == 0:
            nx *= outer
            ny *= outer
        else:
            nx *= inner
            ny *= inner
            
        nx += x
        ny += y
        fout.write('%s, %s\n' % (nx, ny))
    fout.close()

def drawpolygon(n, r, x = 0, y = 0, f = 'output.path'):
    fout = open(f, 'w')
    a = 2*pi / n
    for i in range(n + 1):
        nx = r * cos(a * i) + x
        ny = r * sin(a * i) + y
        fout.write('%s, %s\n' % (nx, ny))
    fout.close()

def drawcircle(r, f = 'output.path'):
    drawpolygon(1000, r)

def drawfunction(func, a, b, x = 0, y = 0, f = 'output.path'):
    fout = open(f, 'w')
    func = func.replace('^', '**')
    nx = a
    while nx <= b:
        exec('ny = ' + func.replace('x',nx))
        fout.write('%s, %s\n' % (nx + x, ny + y))
        nx += 0.5
    fout.close()
        
        
