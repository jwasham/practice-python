from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({!r}, {!r})".format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mult__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


def main():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    print(v1)
    print(v2)
    # assert (v1 + v2) == Vector(4, 5)
    # assert abs( * 3)

if __name__ == "__main__":
    main()
