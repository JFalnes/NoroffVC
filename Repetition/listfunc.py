my_list = [0,1,2,3,4,5,6,7,8,9]

def my_func(my_list):
    for x in my_list:
        yield x
        
for value in my_func(my_list):
    print(value)