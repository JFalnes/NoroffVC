
phonebook = {'Noroff': '38 00 00 00', 'IBM': '49 00 00 00', 'Apple': '23 00 00 00', 
            'GMC': '78 00 00 00', 'Dell': '99 00 00 00'}
print(phonebook['GMC'])

new_com = input('Name of company: ')
new_pn = input('Phone number: ')

phonebook[new_com] = new_pn
print(phonebook)

search_dict = input('Company search: ')

if search_dict in phonebook:
    print(phonebook[search_dict])

for k, v in phonebook.items():
    print(k)