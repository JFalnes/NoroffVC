
my_dict = {'4007': 'Stavanger', '4017': 'Mariero', '4280': 'Skudeneshavn', '4272': 'Veavågen', '4009': 'Eiganes'}

user_input = input('Postal code: ')

if user_input in my_dict:
    print(my_dict[user_input])
else:
    print('Postal code not found')
