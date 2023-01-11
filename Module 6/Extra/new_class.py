
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def output(self):
        return f'My name is {self.name}, age: {self.age}'
    
    def name(self):
        return self.name

a = Person('Johannes', '24')
print(a.output())
del a
try:
    print(a.name())
except:
    pass
b = Person('Simon', '89')
print(b.output())

a = Person('kjasdbuash', '24')
print(a.output())