run_loop = True

my_list = []

while run_loop:
    
    user_input = input('Integer or -1 to quit: ')
    if user_input == '-1':
        print(sum(my_list))
        break
    elif user_input != '-1':
        my_list.append(int(user_input))


print('Exiting loop...')