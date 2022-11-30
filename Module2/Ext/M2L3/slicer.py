
user_input = input('String: ')
ind_start = input('Start index: ')
ind_stop = input('Stop index: ')


if int(ind_stop) > len(user_input):
    print('Index out of range!')
else:
    print(user_input[int(ind_start):int(ind_stop)])

