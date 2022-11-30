
user_input = input('String: ')

user_choice = input('1. Uppercase\n2. Lowercase\n3. Titlecase\n4. Remove front and back whitespaces\n5. Exit\n')

if user_choice == '1':
    print(user_input.upper())
elif user_choice == '2':
    print(user_input.lower())
elif user_choice == '3':
    print(user_input.title())
elif user_choice == '4':
    print(user_input.strip())
elif user_choice == '5':
    exit()