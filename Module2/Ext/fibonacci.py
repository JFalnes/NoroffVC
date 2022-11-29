
first = 0
second = 1
print('second variable; ', second)
length = int(input('How many fib numbers: '))

fib_list = []
fib_list.append(first)
fib_list.append(second)

for x in range(length):

    first = second + first
    fib_list.append(first)
    second = first + second
    fib_list.append(second)


#for x in fib_list:
#    print(x)

print(*fib_list)