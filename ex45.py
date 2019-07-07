"""
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius * self.radius

circle = Circle(10)
print(circle.getArea())
