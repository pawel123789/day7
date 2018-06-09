"""Implementation of Rectangle class"""

class Rectangle:
    """A Rectangle.

    Args:
        width: width of rectangle
        height: height of rectangle
        Both should be positive numbers
        """
    def __init__(self, width, height):
        if width <= 0:
            raise ValueError('Width has to be positive')
        if height <= 0:
            raise ValueError('Height has to be positive')
        self.width = width
        self.height = height

    def area(self):

        return self.height * self.width

    def perimeter(self):

        return 2 * (self.height + self.width)

rect = Rectangle(100, 20)

print('Wysokość: ', rect.height)
print('Obwód to: ', rect.perimeter())
print('Szerokość: ', rect.width)
print('Pole to: ', rect.area())
