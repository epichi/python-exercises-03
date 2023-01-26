import sys 
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = Point(center[0], center[1])
        self.radius = radius

    def __str__(self):
        return f'Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}'

    def contains(self, W):
        if math.sqrt(W.x**2 + W.y**2) <= self.radius:  
            return True
        else: 
            return False



if __name__ == '__main__':
    C = Circle((0, 0), 1)
    A = float(sys.argv[1])
    B = float(sys.argv[2])
    W = Point(A, B)
    if C.contains(W):
        print(
            f'The Point ({W.x}, {W.y}) lies in the Circle of center ({C.center.x}, {C.center.y}) and radius {C.radius}')
    else:
        print(
            f'The Point ({W.x}, {W.y}) lies out of the Circle of center ({C.center.x}, {C.center.y}) and radius {C.radius}')
