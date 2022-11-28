
run_op = True

count = 0

my_list = []

while run_op == True:
    user_input = input('Integer: ')
    print(user_input)

    try:
        int_input = int(user_input)
        if user_input == '-1':
            print(my_list)

            print(sum(my_list))
            run_op = False
        if user_input != '-1':
            my_list.append(int(user_input))
    except ValueError as e:
        print(e)

