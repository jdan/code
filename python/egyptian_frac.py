import sys

if len(sys.argv) != 2:
	sys.exit('Usage: c_frac.py a/b')
	
f = sys.argv[1].split('/')
n = float(f[0]) / int(f[1])

o = n

seq = []

while True:
	a = int(1.0/n) + 1
	seq.append(a)
	n -= 1.0/a
	
	if n == 0:
		break
		
print seq
