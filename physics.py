
from cmath import sqrt
import tkinter as tk


class vector2d(object):

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
        if isinstance(other, vector2d):
            return self.x * other.x + self.y * other.y
        return vector2d(other*self.x,other*self.y)

    __rmul__ = __mul__

    

    def draw(self,canvas,p_vector,tags=None):
        x0 = int(p_vector.x)
        y0 = int(-p_vector.y.real)
        x1 = int((p_vector.x+self.x).real)
        y1 = int(-(p_vector.y+self.y).real)
        canvas.create_line(x0,y0,x1,y1,arrow=tk.LAST, fill='blue', tags=tags)


class Spring():

    def __init__(self, rest, k=0.5, SpingId=None):
        self.rest_length = rest.length
        self.k = k
        self.F = self.force(rest)
        self.SpringID = SpingId


    def excursion(self, v):
        abs_length = v.length - self.rest_length
        try:
            ratio = v.x/v.y
            y = abs_length/sqrt(1+ratio**2)
            if v.y > 0 : y = -y
            x = ratio * y
        except ZeroDivisionError:
            ratio = v.y/v.x
            x = abs_length/sqrt(1+ratio**2)
            if v.x > 0: x = -x
            y = ratio * x
        return vector2d(x,y)

    def force(self, v):
        s = self.excursion(v)
        return self.k * s

    def potential(self, v):
        s = self.excursion(v)
        k = vector2d(1/2*self.k,1/2 * self.k)
        return k * s * s


    def draw(self,Canvas, origin, end):
        if self.SpringID in Canvas.find_all():
            Canvas.coords(self.SpringID,origin.x,-origin.y,end.x,-end.y)
            print(f"Drawed at {origin.x},{-origin.y},{end.x},{-end.y}")
        else:
            self.SpringID = Canvas.create_line(origin.x,-origin.y,end.x,-end.y)

    