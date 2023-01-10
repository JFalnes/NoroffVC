import os


my_list = ['Samsung', 'iPhone', 'OnePlus']

with open('list.txt', 'a') as f:
    for x in my_list:
        f.writelines(x + '\n')

with open('list.txt', 'r') as f:
    for x in f.readlines():
        my_list.append(x)
        print(x.strip())
        print(my_list)

with open('list_other.txt', 'a') as f:
    f.write(str(my_list))
    
try:
  os.remove("demofile.txt")
except FileNotFoundError as e:
  print(f'Error: {e}')
  print('Terminating...')
  quit()
