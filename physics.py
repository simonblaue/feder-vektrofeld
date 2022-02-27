
from cmath import sqrt


class vector2d():

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.length = sqrt(self*self)

    def __str__(self) -> str:
        return str((self.x,self.y))

    def __repr__(self) -> str:
        return str((self.x,self.y))

    def __add__(self,other):
        return vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y