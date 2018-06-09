"""Implementation of Rectangle class"""

class Rectangle:
    """A Rectangle.

    Args:
        width: width of rectangle
        height: height of rectangle
        Both should be positive numbers
        """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

rect = Rectangle(100, 20)
print('Wysokość: ', rect.height)
print('Szerokość: ', rect.width)
print('Pole to: ', rect.area())