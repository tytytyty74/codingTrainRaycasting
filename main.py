import Tkinter
from random import randint
from functions import Vector2D, ellipseArgs, line_length
from boundary import Boundary
from particle import Particle
from ray import Ray
x = 0
y = 0
width = 400
height = 400



def draw():
    while True:
        canvas.delete("all")
        for i in walls:
            i.show(canvas)
        # particle.show(canvas)
        particle.look(walls, canvas)
        particle.update(x, y)
        '''ray.show(canvas)
        ray.lookAt(x, y)
        pt = ray.cast(wall)
        if pt.x > 0 and pt.y > 0:
            args = ellipseArgs(pt.x, pt.y, 8)
            canvas.create_oval(args[0], args[1], args[2], args[3],
                                 fill="white")'''
        canvas.update()

def motion(event):
    global x, y
    x, y = event.x, event.y


root = Tkinter.Tk()
root.bind('<Motion>', motion)
canvas = Tkinter.Canvas(root, width=width, height=height, bg="black")
canvas.pack()
walls = []
for i in range(0, 5):
    x1 = randint(0, width)
    x2 = randint(0, width)
    y1 = randint(0, height)
    y2 = randint(0, height)
    walls.append(Boundary(x1, y1, x2, y2))
walls.append(Boundary(1, 1, width-1, 1))
walls.append(Boundary(width, 0, width, height))
walls.append(Boundary(width, height, 0, height))
walls.append(Boundary(1, height-1, 1, 1))
particle = Particle(100, 100)
root.after(1, draw)
root.mainloop()
