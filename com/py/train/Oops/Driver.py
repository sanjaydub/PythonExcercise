import math
import com.py.train.Oops.Polygon as poly

if __name__ == '__main__':
    print(poly.Polygon.__doc__)
    print(poly.Rectangle.__doc__)
    print(poly.Square.__doc__)
    print(poly.Circle.__doc__)

    # shape=poly.Rectangle(3,4)
    # shape=poly.Square(5)
    # shape=poly.Circle(10)
    shape=poly.RightAngleTriangle(3,4)
    shape.calculateArea()
    shape.calculateParameter()
    shape.printArea()
    shape.printParameter()

    # figures = [poly.Rectangle(3, 4), poly.Square(5), poly.RightAngleTriangle(10, 10)]
    #
    # compFig=poly.CompositFigure(figures)
    # compFig.computeTotalArea()
    # compFig.printArea()
