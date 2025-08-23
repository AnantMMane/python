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

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))