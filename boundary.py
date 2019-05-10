from functions import Vector2D

class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = Vector2D(x1, y1)
        self.b = Vector2D(x2, y2)
    def show(self, canvas):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill="red")
