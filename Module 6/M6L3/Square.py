from TwoDimensionalShape import *

class Square(TwoDimensionalShape):
    def __init__(self, description, length):
        super().__init__(description)

        self.length = length

    def __str__(self):
        return f'Square is a {super().__str__()}'
    
    def area(self):
        return self.length * self.length