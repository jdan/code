#!/usr/bin/python
# Jordan Scales - http://jordanscales.com - http://github.com/prezjordan
# CodeJam 2012 Round 1A

from sys import argv

def main():
    f = open(argv[1])
    n = int(f.readline())
    
    for i in range(n):
        first = f.readline().split()
        typed = int(first[0])
        total = int(first[1])
        p = map(float, f.readline().split())
        
        # get the probabilities for all possible formations of what's currently typed
        # return first index of a wrong character and its probability
        
        res = []
        tryemall(typed, 0, p, -1, 1, res)
        
        # at this point, we have a array containing the probability and first failure
        expected = []
        # now, we're going to append to `expected`
        
        # keep typing = if first_error = -1    total_length - typed + 1
        #               else                   total_length - typed + 1 + total_length (since it's incorrect)
        e = 0
        for item in res:
            if item[1] == -1:
                e += item[0] * (total - typed + 1)
            else:
                e += item[0] * (total - typed + 1 + total + 1)
        expected.append(e)
        
        # press enter right away
        #   the expected value is the length + 2, since hitting enter will be incorrect
        #       then, you need to type it correctly, and hit enter once more
        expected.append(total + 2)
        
        # now, the annoying part => backspaces
        #   you can backspace 1-typed times
        
        # if you hit backspace enough times to get past "first_error", then you can simply type the rest and hit enter
        #   otherwise, you will type the rest, hit enter, enter the whole thing, and hit enter again.
        
        
        for backspaces in range(1, typed+1):
            e = 0
            for item in res:
                if (item[1] == -1) or (typed - backspaces <= item[1]):
                    keystrokes = total - typed + 1 + 2 * backspaces
                    e += item[0] * keystrokes
                else:
                    keystrokes = total - typed + 1 + total + 1 + 2 * backspaces
                    e += item[0] * keystrokes
            expected.append(e)
            
        
        print 'Case #%s: %s' % (int(i + 1), min(expected))
        
# returns an array of 2-arrays containing the probability of the formation, and the index of its first error
def tryemall(typed, count, p, first_error, running_prob, res):
    if (count == typed):
        res.append([running_prob, first_error])
        return

    # the character is right
    tryemall(typed, count+1, p, first_error, running_prob * p[count], res)
    
    # the character is wrong
    if first_error == -1:
        first_error = count
    tryemall(typed, count+1, p, first_error, running_prob * (1 - p[count]), res)
        
if __name__ == '__main__':
    main()
    