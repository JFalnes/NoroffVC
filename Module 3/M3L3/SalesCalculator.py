
sales_value = []

for x in range(10):
    user_input = int(input('Value: '))

    if user_input < 5000:
        continue
    elif user_input > 5000 and user_input < 10001:
        sales_value.append(user_input)

        list_sum = sum(sales_value)
        avg_sum = list_sum / len(sales_value)

        print(f'Total sum: {list_sum}. Total averag: {avg_sum}')
    elif user_input > 10000:
        print('A possible data entry error has occured')