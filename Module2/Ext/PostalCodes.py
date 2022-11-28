
postal_code = {'4017': 'Mariero', '4007': 'Byfjordparken', '4028': 'Dusavik'}

user_select = input('Enter a postcode: ')

if user_select in postal_code:
    print(postal_code[user_select])
else:
    print('Residential area not found!')