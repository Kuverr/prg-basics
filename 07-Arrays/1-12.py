categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

n = 0
m = 0
i = 0
while i < len(expenses):
    if expenses[i] > n:
        n = expenses[i]
        m = i
    i += 1

print(f'Biggest expense is: {categories[m]} equal {expenses[m]}')