
sum = 0

crust_input = input('Crust: ')

if crust_input == 'Thick':
    sum += 10
    print(f'Current price is {sum}')
elif crust_input == 'Thin':
    sum += 5
    print(f'Current price is {sum}')

size_input = input('Size: ')

if size_input == 'Small':
    sum += 30
    print(f'Current price is {sum}')
elif size_input == 'Medium':
    sum += 40
    print(f'Current price is {sum}')
elif size_input == 'Large':
    sum += 50
    print(f'Current price is {sum}')

sauce_input = input('Sauce: ')

if sauce_input == 'Tomato':
    sum += 5
    print(f'Current price is {sum}')
elif sauce_input == 'Barbecue':
    sum += 10
    print(f'Current price is {sum}')

top_input = input('Topping: ')

if top_input == 'Cheese':
    sum += 5
elif top_input == 'Mushrooms':
    sum += 7
    print(f'Current price is {sum}')
elif top_input == 'Avocado':
    sum += 10
    print(f'Current price is {sum}')
elif top_input == 'Pineapple':
    sum += 8
    print(f'Current price is {sum}')
elif top_input == 'Bacon':
    sum += 27
    print(f'Current price is {sum}')
elif top_input == 'Chicken':
    sum += 22
    print(f'Current price is {sum}')
elif top_input == 'Fish':
    sum += 15
    print(f'Current price is {sum}')
elif top_input == 'All':
    sum += 15 + 22 + 27 + 8 + 7 + 10 + 5
    print(f'Current price is {sum}')
elif top_input == 'None':
    print(f'Current price is {sum}')


