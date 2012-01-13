import sys
from random import randint

r = False

if len(sys.argv) < 4:
    sys.exit('Usage: writer.py FILENAME WIDTH HEIGHT (RANDOM: 0/1)')
    
f = file(sys.argv[1], 'w')
w = int(sys.argv[2])
h = int(sys.argv[3])

if len(sys.argv) == 5:
    if sys.argv[4] == '1': r = True

for a in range(h):
    for b in range(w):
        t = 0
        if r:
            t = randint(0, 1)
        f.write(str(t))
        if b < w - 1:
            f.write(' ')
    if a < h - 1:
        f.write('\n')
    
f.close()
