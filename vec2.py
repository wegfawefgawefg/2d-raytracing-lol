import math 
import random

class Vec2:
    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x, y

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def norm(self):
        mag = self.mag()
        if mag > 0:
            return Vec2(
                self.x / mag,
                self.y / mag,
            )
        return self

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def dot(self, vec2):
        return self.x * vec2.x + self.y * vec2.y
    
    def rotate(self, angle):
        return Vec2(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle),
        )

    def __repr__(self):
        return (self.x, self.y, ).__repr__()

    def clone(self):
        return Vec2(self.x, self.y, )

    def clamp(self, low, high):
        return Vec2(
            min(max(self.x, low), high),
            min(max(self.y, low), high),
        )


    def as_tuple(self):
        return (self.x, self.y)

    def as_int_tuple(self):
        return (int(self.x), int(self.y))


    @classmethod
    def random(self):
        return Vec2(
            random.random(), 
            random.random(), 
        )