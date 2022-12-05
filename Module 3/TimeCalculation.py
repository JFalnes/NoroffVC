n = int (input('Minutes: '))
day = int (n // 480)
hours = int (n % 480) // 60
mins = int (n % 480) % 60

print(f'{day}:{hours}:{mins}')