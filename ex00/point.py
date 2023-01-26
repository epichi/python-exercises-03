import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
if __name__ == '__main__': 
    a = input('Insert the coordinates of the first point: ')
    b = input('Insert the coordinates of the second point: ')
    A = eval(a)
    B = eval(b)
    P = Point(A[0], A[1])
    Q = Point(B[0], B[1])
    d = math.sqrt(((P.x - Q.x)**2)+((P.y - Q.y)**2))
    print(f'Their distance is: {d}')
