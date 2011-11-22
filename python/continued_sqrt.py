from math import sqrt
from sys import argv, getrecursionlimit

def main():
    if len(argv) < 2:
        print 'Usage: python continued_sqrt.py [@]LIMIT'
    else:
        limit = argv[1]
        if limit[0] == '@':
            if int(limit[1:]) + 1 >= getrecursionlimit():
                print 'Sorry, maximum stack depth exceeded.'
                print 'Limit[%s]: :(' % int(limit[1:])
            else:
                for limit in range(1, int(limit[1:]) + 1):
                     print 'Limit[%s]: %s' % (limit, c_sqrt(limit))
        else:
            print 'Limit[%s]: %s' % (int(limit), c_sqrt(int(limit)))

def c_sqrt(limit, n=0):
    if limit >= getrecursionlimit():
        print 'Sorry, maximum stack depth exceeded.'
        return ':('
        
    if limit == 0:
        return n
    return n + sqrt(c_sqrt(limit-1, n+1))
    
if __name__ == '__main__':
    main()