import sys
from time import sleep

b = False

if len(sys.argv) < 2:
    sys.exit("Please include an initial condition file.")
    
if len(sys.argv) == 3:
    if sys.argv[2] == '1':
        b = True
    
master = []
    
f = file(sys.argv[1])

for line in f.readlines():
    master.append([])
    l = line.split(' ')
    for a in l:
        master[len(master) - 1].append(int(a))
        
f.close()
        
x = len(master)
y = len(master[0])

def get_neighbors(loc):
    width = y - 1
    height = x - 1
    result = []
    for a in range(loc[0] - 1, loc[0] + 2):
        for b in range(loc[1] - 1, loc[1] + 2):
            if a == loc[0] and b == loc[1]:
                pass
            else:
                if a >= 0 and b >= 0 and a <= height and b <= width:
                    if master[a][b] > 0:
                        result.append([a, b])
    return result
        
def output(m, f = False):
    s = ''
    for a in m:
        for b in a:
            if f == False:
                s += str(b) + ' '
            else:
                t = ' '
                if b == 1:
                    t = 'X'
                s += t + ' '
        s += '\n'
    print s
    
#  0 => no cell
#  1 => cell
#  2 => cell that will die
# -1 => (new) cell that will appear
    
def tick():
    for r in range(x):
        for c in range(y):
            pop = len(get_neighbors([r, c]))
            
            if pop < 2 or pop > 3: #population error
                if master[r][c] == 1: 
                    master[r][c] = 2 #kill it
                    
            if pop == 3:
                if master[r][c] == 0: 
                    master[r][c] = -1 #spawn one
                
    # done. now fix all changes
    for r in range(x):
        for c in range(y):
            master[r][c] = abs(master[r][c]) % 2
            
    output(master, b)
    
output(master, b)
while(True):
    sleep(0.1)
    tick()
