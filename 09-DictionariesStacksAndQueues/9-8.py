price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key,data in price_list.items():
    print(f'{key}: {data}')

sum1 = 0
for data in price_list.values():
    sum1 += data
print(f'Total product value: {sum1}')

for key,data in price_list.items():
    price_list[key] = data * 0.9

print('Reduced product prices:')
for key,data in price_list.items():
    print(f'{key}: {data}')

sum2 = 0
for data in price_list.values():
    sum2 += data
print(f'Total product value: {sum2}')