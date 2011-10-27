from Tkinter import *

cols = ["orange", "yellow", "red", "blue", "white"]

def mandel(c):
        z = 0
        i = 0
        for h in range(0,20):
            z = z**2 + c
            if abs(z) > 2:
                return cols[i / 4 - 1]
            i += 1
        return "black"

root = Tk()
w = Canvas(root, width=600,height=600)
w.pack()

for hx in range(0,600,75):
    w.create_line(0,hx,600,hx,fill="blue")

for hy in range(0,600,75):
    w.create_line(hy,0,hy,600,fill="blue")

print "Initializing..."

for x in range(0,600):
    real = x / 200.0 - 1.5
    for y in range(0,600):
        img = y / 200.0 - 1.5
        c = complex(real, img)
        col = mandel(c)
        w.create_line(x,600-y,x+1,601-y,fill=col)
        w.pack()

print "Complete!"

root.mainloop()    
