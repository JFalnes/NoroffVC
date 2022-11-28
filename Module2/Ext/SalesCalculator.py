my_list = []

for i in range(10):
    sales_value = int(input('Value: '))
    if sales_value < 5000:
        break
    
    elif sales_value > 5000 and sales_value < 10001:
        my_list.append(sales_value)
        print(f'Total sales average: {sum(my_list) / len(my_list)}')
        print(f'Current sales total: {sum(my_list)}')

    elif sales_value >= 10001:
        print('Possible data entry error!')
    

