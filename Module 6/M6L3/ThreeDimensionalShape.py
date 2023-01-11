from Shape import *

class ThreeDimensionalShape(Shape):

    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return f'Three-dimensional Shape\n{super().__str__()}'
