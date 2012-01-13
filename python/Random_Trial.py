from sys import argv
from random import randint

m = int(argv[1])

print 'Press Ctrl-C anytime to quit.'

trial = 1
count = 0
record = 0
while True:
    if randint(0,1) == 1:
        count += 1
        if count > record: 
            record = count
            r = (0.5) ** record * trial
            print '%s Trials. Record: %s => %s' % (trial, record, r)
    else:
        count = 0
        
    if trial == m:
        break
        
    trial += 1
