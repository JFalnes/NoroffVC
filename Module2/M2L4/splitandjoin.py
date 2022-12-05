
user_input = input('String: ')
split_char = input('Character: ')

new_string = user_input.split(split_char)
print(new_string)
join_char = input('Join: ')
print(join_char.join(new_string))