hardware = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

for key,data in hardware.items():
    print(f'Number of {key}s : {data}')

sum = 0
for data in hardware.values():
    sum += data

print(f'Total number of items in the store: {sum}')