
def start():
    print('Starting')

def my_func(name, age, eyes):
    try:
        print(name, age + 2, eyes)
    except TypeError as e:
        print(f'Error: {e}. Try again!')
        start()


my_func('Johannes', '24', 'Blue')
