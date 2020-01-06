import math


class Polygon:
    """This is the polygon class, should be abstract"""

    # parameter
    # area
    def __init__(self):
        self.area = 0
        self.para = 0

    def calculateArea(self):
        pass

    def calculateParameter(self):
        pass

    def printArea(self):
        print("Area is %s square units" % self.area)

    def printParameter(self):
        print("Area is %s units" % self.para)

    @property
    def getArea(self):
        return self.area

class Rectangle(Polygon):
    "This is a reactangle class - concrete"

    def __init__(self, len, bre):
        self.len = len
        self.bre = bre

    def calculateArea(self):
        self.area = self.len * self.bre

    def calculateParameter(self):
        self.para = 2 * (self.len + self.bre)


class Square(Rectangle):
    "This is a Square, inheriting Rectangle class - concrete"

    def __init__(self, side):
        self.side = side
        super(Square, self).__init__(self.side, self.side)


class Circle(Polygon):
    "This is a Circle class - concrete"

    def __init__(self, rad):
        self.rad = rad

    def calculateArea(self):
        self.area = 3.14 * self.rad * self.rad

    def calculateParameter(self):
        self.para = 2 * 3.14 * self.rad


class RightAngleTriangle(Polygon):
    "This is a Circle class - concrete"

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calculateArea(self):
        self.area = .5 * self.b * self.h

    def calculateParameter(self):
        self.para = self.b + self.h + math.sqrt(self.b * self.b + self.h * self.h)


class CompositFigure:
    "This class is to calculate area of composit figure"

    def __init__(self, listoffigs):
        self.listOfFigs = listoffigs
        self.totalArea=0

    def computeTotalArea(self):
        for obj in self.listOfFigs:

            obj.calculateArea()
            self.totalArea=self.totalArea+obj.area

    # self.totalArea=self.totalArea+fig.getArea

    def printArea(self):
        print("Total Area of the composite figure is  %s square units" % self.totalArea)