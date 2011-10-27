from Tkinter import *
def mandel(c):
    z=0
    for h in range(0,20):
        z = z**2 + c
        if abs(z) > 2:
            break
    if abs(z) >= 2:
        return 0
    else:
        return 1

root = Tk()
w = Canvas(root, width=1200,height=1200)
w.pack()

for hx in range(0,1200,300):
    w.create_line(0,hx,1200,hx,fill="blue")

for hy in range(0,1200,300):
    w.create_line(hy,0,hy,1200,fill="blue")

for x in range(0,1200):
    real = x / 300.0 - 2.0
    for y in range(0,1200):
        img = y / 300.0 - 2.0
        c = complex(real, img)
        if mandel(c) == 1:
            w.create_line(x,1200-y,x+1,1200-y+1,fill="black")
            w.pack()

root.mainloop()
