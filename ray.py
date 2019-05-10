from functions import Vector2D, VectorFromAngle
class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = VectorFromAngle(angle)

    def lookAt(self, x, y):
        self.dir = Vector2D(x-self.pos.x, y-self.pos.y)
    def show(self, canvas):
        canvas.create_line(self.pos.x, self.pos.y,
                           self.pos.x+self.dir.x*10, self.pos.y+self.dir.y*10,
                           fill="red")

    def cast(self, wall):
        retval = Vector2D(-1.0, -1.0)
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y
        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x+self.dir.x
        y4 = self.pos.y+self.dir.y
        den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if not den == 0:
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = -((x1 - x2) * (y1 - y4) - (y1 - y2) * (x1 - x3)) / den
            if 1 > t > 0 and u > 0:
                retval = Vector2D(x1+t*(x2-x1), y1+t*(y2-y1))
        return retval
