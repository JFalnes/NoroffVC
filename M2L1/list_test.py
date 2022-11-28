friend_list = []

count = 0

for x in range(10):
    count += 1
    friend_name = input(f'{count}. Friends name: ')
    friend_list.append(friend_name)
friend_list.sort()
print(friend_list)
search_name = input('Name to search: ')

if search_name in friend_list:
    print(friend_list.index(search_name))
    friend_list.reverse()
    print(friend_list)
    print(friend_list[:5])
else:
    print('The name does not exist')

new_name = input('Another one: ')
friend_list.append(new_name)
print(friend_list)