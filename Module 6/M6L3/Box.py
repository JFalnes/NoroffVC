from ThreeDimensionalShape import *

class Box(ThreeDimensionalShape):

    def __init__(self, description, length, width, height):
        super().__init__(description)
        self.length = length
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Box is a {super().__str__()}'

    def area(self):
        return (self.length * self.width * 2) + \
               (self.length * self.height * 2) + \
               (self.width * self.height * 2)

               
    def volume(self):
        return self.length * self.width * self.height
