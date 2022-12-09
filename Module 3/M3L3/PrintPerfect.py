max_value = int(input('Max value: '))
current = 1

perfect_number = []

while current <= max_value:
    total = 0 
    for i in range(1, current):
        if current % i == 0:
            total += i

    if total == current:
        perfect_number.append(current)
        print(current)
    
    current += 1

print(*perfect_number)

