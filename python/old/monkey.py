## Monkey.py by Jordan Scales (scalesjordan@gmail.com, http://ilictronix.com)
## Date: 4/2/2010
##
## Description: Takes a string and randomly types keys until the desired
##     string has been typed (in order)
##
## Tips: Python is pretty damn slow, so don't try anything
##     too out of the ordinary. Only a few letters is practical.

from random import randint

goal = str(raw_input('Enter a string for the monkey to type: ')).lower()
current = ''
count = 0

def format(number):                  # just adds commas to the number
    final = ''
    string = str(number)
    length = len(string)
    instances = (length - 1) / 3
    if length % 3 == 0:              # choose a good starting point
        start = 3                    # place of first comma
    else:
        start = length % 3
    
    final += string[:start]          # gradually piece together the string
    for i in range(instances):       #     with commas
        pos = start + i * 3
        final += ',' + string[pos:pos+3]
        
    return final
        

print 'The monkey is typing...'

while current <> goal:                       # strings should be same length 
    count += 1
    current += chr(randint(0,25) + 97)       # add a random letter
    
    if len(current) > len(goal):
        current = current[-(len(goal)):]     # trim off what wastes memory

print 'It took the monkey %s keystrokes to type "%s"' % (format(count), goal)

