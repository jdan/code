from sys import argv

m = int(argv[1])
d = {}

def digitsum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digitsum(n / 10)

for i in range(1, m + 1):
    val = digitsum(i)
    if val in d:
        d[val] += 1
    else:
        d[val] = 1
        
for a, b in enumerate(d):
    print '%s: %s' % (b, d[b])
