# Julia Set generator by Jordan Scales
# 12/02/2009

from Tkinter import *

cols = ["orange", "yellow", "red", "blue", "white"]

# favorites... 
# -0.8+0.156j
# -0.70176-0.3842j
# -0.4+0.6j
# -0.835-0.2321j

eq = -0.8+0.156j
iter = 50

def julia(t, c):
    z = t
    i = 0
    for h in range(0, iter):
        z = z**2 + c
        if abs(z) > 2:
            return cols[i / 10 - 1]
        i += 1
    return "black"

root = Tk()
w = Canvas(root, width=600, height=600)
w.pack()

for hx in range(0, 600, 75):
    w.create_line(0,hx,600,hx,fill="blue")

for hy in range(0, 600, 75):
    w.create_line(hy,0,hy,600,fill="blue")

print 'Loading...'

for x in range(0, 600):
    real = x / 200.0 - 1.5
    for y in range(0, 600):
        img = y / 200.0 - 1.5
        com = complex(real, img)
        col = julia(com, eq)
        w.create_line(x, 600-y, x+1, 600-y+1, fill=col)
        w.pack()
            
print 'Done!'

root.mainloop()
