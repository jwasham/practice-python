from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt


Point = namedtuple('Point', 'x y')


class ConvexHull(object):
    points = []

    def __init__(self):
        pass

    def add(self, point):
        self.points.append(point)

    def display(self):
        x = [p.x for p in self.points]
        y = [p.y for p in self.points]

        plt.plot(x, y, marker='D', linestyle='None')
        plt.title('Convex Hull')
        plt.show()


def main():
    ch = ConvexHull()
    ch.add(Point(1, 4))
    ch.add(Point(3, 12))
    ch.add(Point(5, 7))
    ch.add(Point(3, 6))
    ch.add(Point(12, 19))
    ch.add(Point(4, 8))
    ch.add(Point(5, 7))
    ch.add(Point(9, 3))
    ch.add(Point(9, 6))
    ch.add(Point(10, 6))
    ch.add(Point(8, 16))
    ch.add(Point(2, 6))

    ch.display()


if __name__ == '__main__':
    main()
