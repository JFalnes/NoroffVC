underscore = '-' * 25
print(f'{underscore}\nMenu System\n{underscore}\n1. Guess the number\n2. Calculate time\n3. Print something\n4. Change a print option\n5. Quit')

message = ['Coding is fun', 'Python is not code, but a way of life','We learn Python the fun way','We code, because we can'] 

user_choice = int(input('Choice: '))

if user_choice == 1:

    user_num = int(input('Number: '))
    if user_num == 543:
        print('You guessed the number! It is 543')
    elif user_num < 543:
        print('The number is too low')
    elif user_num > 543:
        print('The number is too high')

elif user_choice == 2:
    user_time = input('Datetime: ')
    new_time = user_time[:-3]
    if int(new_time) > 8 and int(new_time) < 17:
        print('Inside working hours')
    elif int(new_time) >= 0 and int(new_time) <= 24:
        print('Private time')
    else:
        print('Invalid input')

elif user_choice == 3:
    user_index = input('Enter a value between 0 and 3: ')
    print(message[int(user_index)])

elif user_choice == 4:
    user_index = input('Enter a value between 0 and 3: ')
    user_text = input('New text: ')
    message[int(user_index)] = user_text
    print(message)

elif user_choice == 5:
    exit()
