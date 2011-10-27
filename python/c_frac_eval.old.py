from sys import argv

m = 20

pattern = argv[1].split(';')
tail = map(int, pattern[1].split(',') * m)

r = [int(pattern[0])] + tail

def c_frac(r):
    if len(r) == 1:
        return 1.0 / r[0]
    else:
        return r[0] + 1.0 / c_frac(r[1:])

print c_frac(r)
