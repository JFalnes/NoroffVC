import time

num1 = input('Number 1: ')
num2 = input('Number 2: ')


start = time.time()

time_to_sleep = int(num1)+int(num2)
time.sleep(time_to_sleep)
end = time.time()

result = end - start
print('{0:.2f}'.format(result))
