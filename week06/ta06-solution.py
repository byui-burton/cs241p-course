"""
File: ta06-solution.py
Author: Br. Burton

This program demonstrates inheritance to define a circle
that inherits from a point.
"""


class Point:
    """
    A Point has an x and y coordinate.
    """
    def __init__(self):
        self.x = 0
        self.y = 0

    def prompt_for_point(self):
        self.x = float(input("Enter x: "))
        self.y = float(input("Enter y: "))

    def display(self):
        print("({}, {})".format(self.x, self.y))


class Circle(Point):
    """
    A Circle has an x and y, plus a radius.
    """
    def __init__(self):
        super().__init__() # don't forget to call the point __init__
        self.radius = 0

    def prompt_for_circle(self):
        self.prompt_for_point() # call the point method
        self.radius = float(input("Enter radius: "))

    def display(self):
        print("Center:")
        super().display() # call the point method
        print("Radius: {}".format(self.radius))


def main():
    """
    Test our classes from above.
    :return:
    """
    c = Circle()
    c.prompt_for_circle()

    print()

    c.display()

if __name__ == "__main__":
    main()