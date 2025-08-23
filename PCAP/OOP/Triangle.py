from math import hypot

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def distance_from_point(self, other):
        return hypot(self.__x - other.__x, self.__y - other.__y)
    
    def distance_from_xy(self, x, y):
        return hypot(self.__x - x, self.__y - y)
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
class Triangle:
    def __init__(self, p1, p2, p3):
        if not all(isinstance(p, Point) for p in (p1, p2, p3)):
            raise TypeError("All arguments must be Point instances")
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def perimeter(self):
        return (self.__p1.distance_from_point(self.__p2) +
                self.__p2.distance_from_point(self.__p3) +
                self.__p3.distance_from_point(self.__p1))
    
    def area(self):
        a = self.__p1.distance_from_point(self.__p2)
        b = self.__p2.distance_from_point(self.__p3)
        c = self.__p3.distance_from_point(self.__p1)
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

assert (triangle.perimeter() == 3.414213562373095)