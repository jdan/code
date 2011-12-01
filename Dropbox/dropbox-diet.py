#!/usr/bin/python

## The Dropbox Diet
## by Jordan Scales
##
##   scalesjordan@gmail.com
##   http://jordanscales.com
##   http://github.com/prezjordan
##
## 11/30/11

# globals (better organization so I could make this cleaner)
cases = []
n = 0
p = []

# I should use longer variables but this is only a quick hack-together
def prime_list(n): 
    r = [2] # start off with 2
    c = 1   # how many primes we've found
    d = 3   # current number
    while c < n:  # while we're still below n primes
        o_d = d   # store d
        for p in r:
            if not d % p:
                d += 2 # change d and get out
                break
        if o_d < d:  # did we break?
            continue
        r.append(d) # we've got a prime
        d += 2      # why check evens? skip 'em
        c += 1      # add 1 to our count of primes
    
    return r
    
def find_sequence(index, s, u): # index of cases, running total, unique id (made of primes)
    if u > 1:
        if s == 0:
            return u  # if a number is found, return the unique id
            
    if index >= n:
        return 0   # if we haven't found anything, go ahead and return 0
    
    # check yourself, and skip yourself (pruning the tree if needed by or'ing results)
    return find_sequence(index + 1, s + cases[index][1], u * p[index]) or \
            find_sequence(index + 1, s, u)

def main():
    global cases, n, p
    
    n = int(raw_input())  # get the amount of inputs we'll be checking
    cases = [raw_input().split(' ') for i in range(n)]  # throw all the inputs into an array
    for i, case in enumerate(cases):  
        cases[i][1] = int(cases[i][1])  # convert the second item of each input to an int
        
    p = prime_list(n)   # get a prime list (to use later)
    k = find_sequence(0, 0, 1)  # call find_sequence initially
    result = []
    
    if k == 0:
        result = ['no solution']
    else:
        # decode k
        # find_sequence will return a product of primes
        #    so we can easily identify which items we used to achieve a sum of 0
        for i, prime in enumerate(p):
            if not k % prime:
                k /= prime
                result.append(cases[i][0])
        
    print '\n'.join(result)
    
if __name__ == '__main__':
    main()