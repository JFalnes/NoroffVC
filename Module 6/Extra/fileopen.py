with open('newfile.txt', 'w') as f:
    f.write('This is a brand new file\n')

with open('newfile.txt', 'a') as f:
    f.write('This is an appendage\n')

with open('myfile.txt', 'r') as f:
    text = f.readlines()

    print(type(text))
    count = 0
    for x in text:
        count += 1
        name = x.strip()
        print(f'{count} name: {name}')

