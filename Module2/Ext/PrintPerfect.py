max_value = int(input('Max value: '))
current = 1

while current <= max_value:
    total = 0
    for i in range(1, current):
        if current % i == 0:
            total += i

    if total == current:
        print(current)

    current += 1
