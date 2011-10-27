import sys

if len(sys.argv) <> 2:
	print 'Please enter a sequence of characters to permutate.'
	sys.exit(0)

letters = sys.argv[1]
s = len(letters)
a = []
possible = []

for c in range(s):
    a.append('')
    possible.append(0)    

def permutate(n):
    for i in range(s):
        if possible[i] == 0:
            possible[i] = 1
            a[n - 1] = letters[i]
            if n < s:
                permutate(n+1)
            else:
                print ''.join(a)                        
                
            possible[i] = 0

permutate(1)
