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


if __name__ == '__main__':
    print(Circle((150, 100), 75))
