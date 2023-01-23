from Square import * 
from Rectangle import *
from Box import *
from Cube import *

shapes = []

shapes.append(Square("Square 1", 10))
shapes.append(Square('New Square', 17))

shapes.append(Rectangle('Rectangle 2', 10, 25))
shapes.append(Box('Box 1', 20, 10, 5))
shapes.append(Cube('Cube 1', 10))

print('Number of shapes: ', Shape.count)
print('-' * 50)
print(id(Rectangle('Desc', 12, 25)))

for current in shapes:
    print(current)
    print('-' * 50)

print(id(Square('Desc', 12)))
