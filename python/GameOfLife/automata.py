import sys
from time import sleep

if len(sys.argv) < 2:
    print("USAGE: python automata.py FILE RULES(LIVE/SPAWN)")
    sys.exit("Example: python automata.py maze_template 12345/3")

rules = sys.argv[2].split('/')
live  = rules[0]
spawn = rules[1]

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

def output(m):
    s = ''
    for a in m:
        for b in a:
            t = ' '
            if b == 1:
                t = '\033[44m \033[0m'
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

            if str(pop) not in live: #population error
                if master[r][c] == 1:
                    master[r][c] = 2 #kill it

            if str(pop) in spawn:
                if master[r][c] == 0:
                    master[r][c] = -1 #spawn one

    # done. now fix all changes
    for r in range(x):
        for c in range(y):
            master[r][c] = abs(master[r][c]) % 2

    output(master)

output(master)
while(True):
    sleep(0.1)
    tick()
