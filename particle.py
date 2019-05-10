from functions import Vector2D, ellipseArgs, line_length
from ray import Ray
from math import radians
class Particle:
    def __init__(self, x, y):
        self.pos = Vector2D(x, y)
        self.rays = []
        for i in range(0, 1440):
            self.rays.append(Ray(self.pos, radians(i/4.0)))

    def update(self, x, y):
        self.pos = Vector2D(x, y)
        for i in self.rays:
            i.pos = Vector2D(x, y)

    def look(self, walls, canvas):
        points = []
        for ray in self.rays:
            record=float("inf")
            closest = Vector2D(-1, -1)
            for wall in walls:
                pt = ray.cast(wall)
                if pt.x > 0 and pt.y > 0:
                    d = line_length(self.pos, pt)
                    if d < record:
                        record = d
                        closest = pt
            if closest.x > 0 and closest.y > 0:
                points.append(closest.x)
                points.append(closest.y)
        canvas.create_polygon(points, fill="white")

    def show(self, canvas):
        args = ellipseArgs(self.pos.x, self.pos.y, 4)
        canvas.create_oval(args[0], args[1], args[2], args[3], fill="white")
        for i in self.rays:
            i.show(canvas)