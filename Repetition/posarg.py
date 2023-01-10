
# Positional Arguments
# Keyword/Value Arguments
# Default Values

def my_func(book, name, age=0):
    if age == 0:
        print(book, name)
    else:    
        print(name, book, age)

my_func('book', name='Johannes', age=24)