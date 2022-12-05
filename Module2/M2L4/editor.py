user_input = input('String: ')

print(f'Length of string: {len(user_input)}')

user_index = input('Index: ')

my_list = user_input.split()

try:
    words = user_input.split(" ")
    words[int(user_index)] = f'"{words[int(user_index)]}"'
    print(" ".join(words))

except ValueError as e:
    print(f'Error {e}')

# Get index value based on string input
# user_word = input('Word: ')
# print(my_list.index(user_word))