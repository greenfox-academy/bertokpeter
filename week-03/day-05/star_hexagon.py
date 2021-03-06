from tkinter import *
import math
root = Tk()

canvas_width = 600
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

w = canvas_width/2
x = canvas_width/2
y = canvas_height/2

def triangle_height(size):
     return math.sqrt(size**2-(size/2)**2)

def star_hexagon(x,y,w):
    if w < 2.5:
        pass
    else:
        initx = x-w/2
        h = triangle_height(w)
        canvas.create_polygon(initx, y-h, initx+w, y-h, initx+1.5*w, y,
        initx+w, y+h, initx, y+h, initx-w/2, y, outline="black", width=1, fill="")
        star_hexagon(x-w/3, y-h*2/3, w/3)
        star_hexagon(x+w/3, y-h*2/3, w/3)
        star_hexagon(x+w*2/3, y, w/3)
        star_hexagon(x+w/3, y+h*2/3, w/3)
        star_hexagon(x-w/3, y+h*2/3, w/3)
        star_hexagon(x-w*2/3, y, w/3)

star_hexagon(x,y,w)

root.mainloop()