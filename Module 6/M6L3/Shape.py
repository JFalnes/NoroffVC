
class Shape:
    count = 0

    def __init__(self, description):
        self.description = description
        Shape.count += 1

    def __str__(self):
        return f'{self.description}\nArea:\t{self.area()}\tVolume: {self.volume()}'
    
    def area(self):
        return 0
    
    def volume(self):
        return 0