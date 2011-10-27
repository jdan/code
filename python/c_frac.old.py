import sys

if len(sys.argv) != 2:
	sys.exit('Usage: c_frac.py a/b')
	
f = sys.argv[1].split('/')
n = float(f[0]) / int(f[1])

frac = []

while True:
	a = int(n)
	frac.append(a)
	
	n -= a
	if n < 0.0001: break
	n = 1.0/n
	
	if n == int(n):
		frac.append(n)
		break
		
# print (ugly)
	
s = '['
s += str(frac[0]) + ';'

for i in frac[1:]:
	s += str(i) + ','
	
s += '\b'
s += ']'

print s
