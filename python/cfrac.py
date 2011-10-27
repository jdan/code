def expand(n):
    frac = []
    while True:
        a = int(n)
        frac.append(a)

        n -= a
        if n < 0.0001: break
        n = 1.0/n

        if n == int(n):
            frac.append(int(n))
            break
    return frac

def compress(frac):
    n = frac[-1]
    d = 1
    for i in range(2, len(frac)+1):
        # XOR swap
        n = n ^ d
        d = n ^ d
        n = n ^ d
        n += d * frac[-i]
    return [n, d]

##k = str(raw_input('Enter a fraction [a/b]: ')).split('/')
##v = float(int(k[0])) / int(k[1])
##
##f = expand(v)
##print 'Continued fraction: %s' % f
##
##g = compress(f)
##print 'Compressed: %s/%s' % (g[0], g[1])
