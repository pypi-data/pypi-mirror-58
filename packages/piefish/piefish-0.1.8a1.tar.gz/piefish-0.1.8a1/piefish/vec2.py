from math import sqrt, sin, cos, atan, pi

class vec2:
    @staticmethod
    def fromPolar(self, r, theta): 
        """Creates a new vector from polar coordinates."""
        return vec2(r * cos(theta), r * sin(theta))
    def __init__(self, x, y): self.x = x ; self.y = y
    def __add__(self, other): return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other): return vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other): return vec2(self.x * other, self.y * other)
    def __div__(self, other): return vec2(self.x / other, self.y / other)
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __str__(self): return f"({self.x}, {self.y})"
    def __repr__(self): return f"vec2({self.x}, {self.y})"
    @property
    def argument(self):
        """Returns the angle between the vector and positive x in radians (mod 2 * pi)."""
        if self.x == 0:
            if self.y == 0: return 0
            if self.y > 0: return (0.5 * pi)
            return (1.5 * pi)
        if self.x < 0: return pi + atan(self.y / self.x)
        if self.x > 0 and self.y < 0: return 2 * pi + atan(self.y / self.x)
        return atan(self.y / self.x)
    @property
    def magnitude(self): 
        """Returns the length of the vector (distance from point to origin)."""
        return sqrt(self.x ** 2 + self.y ** 2)
    @property
    def tpl(self):
        """Returns the vec2 as a tuple."""
        return (self.x, self.y)
    @staticmethod
    def dot(a, b): 
        """Returns the dot product of 2 vectors"""
        return a.x * b.x + a.y * b.y
    def normalize(self): 
        """Returns the normalized vector."""
        return self / self.magnitude
    def get_normal(self): 
        """Returns vector perpendicular on the current vector (relative to the origin)."""
        return vec2(-self.y,self.x)
    def rotate(self, theta): 
        """Rotates the vector by theta radians."""
        self.x = self.x * cos(theta) - self.y * sin(theta)
        self.y = self.x * sin(theta) + self.y * cos(theta)