# Julia Set generator by Jordan Scales
# 12/02/2009

from Tkinter import *

# favorites... 
# -0.8+0.156j
# -0.70176-0.3842j
# -0.4+0.6j
# -0.835-0.2321j

eq = -0.8+0.156j
iter = 50

def julia(t, c):
    z = t
    for h in range(0, iter):
        z = z**2 + c
        if abs(z) > 2:
            break
    return abs(z) < 2

root = Tk()
w = Canvas(root, width=1200, height=1200)
w.pack()

for hx in range(0, 1200, 300):
    w.create_line(0,hx,1200,hx,fill="blue")

for hy in range(0, 1200, 300):
    w.create_line(hy,0,hy,1200,fill="blue")

print 'Loading...'

for x in range(0, 1200):
    real = x / 300.0 - 2.0
    for y in range(0, 1200):
        img = y / 300.0 - 2.0
        com = complex(real, img)
        if julia(com, eq):
            w.create_line(x, 1200-y, x+1, 1200-y+1, fill="black")
            w.pack()
            
print 'Done!'

root.mainloop()
