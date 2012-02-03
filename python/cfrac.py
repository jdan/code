#!/usr/bin/python
from sys import argv

def sqrt_cont_frac(n):
    head = int(n**0.5)
    if head == n**0.5:
        return '[%s]' % str(head)
    
    num = head
    denom = n - head**2
    
    a = [head]
    states = []
    
    while 1:
        pull = (head + num) / denom
        num -= pull*denom
        
        for state in states:
            if state == [pull, num, denom]:
                return '[%s;(%s)]' % (str(head), ','.join(map(str, a[1:])))
                
        states.append([pull, num, denom])
        a.append(pull)
        
        denom = (n - num**2) / denom
        num *= -1
        
if __name__ == '__main__':
    if len(argv) < 2:
        n = int(raw_input('n = ?: '))
    else:
        n = int(argv[1])
        
    print 'sqrt(%s) => %s' % (n, sqrt_cont_frac(n))