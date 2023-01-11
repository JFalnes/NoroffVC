from TwoDimensionalShape import *

class Rectangle(TwoDimensionalShape):

    def __init__(self, description, length, width):
        super().__init__(description)
        self.length = length
        self.width = width

    def __str__(self):
        return f'Rectangle is a {super().__str__()}'

    def area(self):
        return self.length * self.width
        