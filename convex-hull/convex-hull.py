from collections import namedtuple
import matplotlib.pyplot as plt
import random


Point = namedtuple('Point', 'x y')


class ConvexHull(object):
    _points = []
    _hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        self._points.append(point)

    def _get_orientation(self, origin, p1, p2):
        '''
        Returns the orientation of the Point p1 with regards to Point p2 using origin.
        :param p1:
        :param p2:
        :return: integer
        '''
        difference = (
                    ((p2.x - origin.x) * (p1.y - origin.y))
                    - ((p1.x - origin.x) * (p2.y - origin.y))
                )

        return difference

    def compute_hull(self):
        '''
        Computes the convex hull and returns the points on the hull.
        :return:
        '''
        points = sorted(self._points, key=lambda temp_point: temp_point.x)

        start = points[0]
        point = points[0]
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def display(self):
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='D', linestyle='None')

        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)

        plt.title('Convex Hull')
        plt.show()


def main():
    ch = ConvexHull()
    # for _ in range(10):
    #     ch.add(Point(random.randint(0, 100), random.randint(0, 100)))

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

    ch.compute_hull()
    ch.display()


if __name__ == '__main__':
    main()
