def to_bin(n, cap = 10):
	c = 0
	a = []
	while c <= cap:
		n *= 2
		if n >= 1:
			a.append(1)
			n -= 1
			if c == 0:
				c = 1
		else:
			a.append(0)
		if c >= 1:
			c+= 1
	s = ''
	i = 0
	while a[i] != 1:
		i += 1
	s = '1.%s x 2^-%s' % (''.join(map(str, a[i+1:])), i+1)
	return s

print to_bin(0.1415926535897932384626, 51)
