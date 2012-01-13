from math import pi

def sigma(f,a,b):
    t = 0
    for i in range(a, b+1):
        t += f(i)
    return t
    
x_sq = lambda x : x**2
i_n_sq = lambda n : 1.0/n**2
i_n = lambda n : 1.0/n

print sigma(i_n_sq, 1, 10000)
print pi**2 / 6
