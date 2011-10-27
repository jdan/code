from Tkinter import *

def mandel(c):
        z=0
        for h in range(0,20):
            z = z**2 + c
            if abs(z) > 2:
                break
        if abs(z) >= 2:
            return False
        else:
            return True

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
        if mandel(c):
            w.create_line(x,600-y,x+1,601-y,fill="black")
            w.pack()

print "Complete!"

root.mainloop()    
