from Shape import *


class TwoDimensionalShape(Shape):

    def __init__(self, description):
        super().__init__(description)
    
    def __str__(self):
        return f"Two-dimensional shape\n{super().__str__()}"
        
