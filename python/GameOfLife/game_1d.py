import sys
import random
from time import sleep

master = []
width = 0
gap = 0.5
    
def init():
    global gap
    global width
    width = int(sys.argv[1])
    if len(sys.argv) == 3:
        gap = 1.0 / int(sys.argv[2])

    for i in range(width):
        master.append(random.randint(0,1))
        
    output(master)
    sleep(gap)
        
def tick():
    for i in range(width):
        pop = 0
        
        if i > 0:
            if master[i-1] > 0: 
                pop += 1
                
        if i < width - 1:
            if master[i+1] > 0: 
                pop += 1
            
        if master[i] == 1:
            master[i] = 2
        else:
            if pop == 1: 
                master[i] = -1

    for a in range(width):
        master[a] = abs(master[a]) % 2
            
    output(master)
    
def output(m):
    s = ''
    for a in m:
        if a == 1:
            s += 'X'
        else:
            s += ' '
    print s        
    
def output2(m):
    s = ''
    for a in m:
        s += str(a)
    print s
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: game_1d.py WIDTH [FPS]')
        
    init()
    
    while True:
        tick()
        sleep(gap)
