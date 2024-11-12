# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

food = 0
for i in monthly_expenses:
    food += i[0]
tran = 0
for i in monthly_expenses:
    tran += i[1]
util = 0
for i in monthly_expenses:
    util += i[2]


w1 = sum(monthly_expenses[0])
w2 = sum(monthly_expenses[1])
w3 = sum(monthly_expenses[2])
w4 = sum(monthly_expenses[3])

monthly_expenses = w1 + w2 + w3 + w4

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', tran)
print('Utilities:', util)
print('Week 1:', w1)
print('Week 2:', w2)
print('Week 3:', w3)
print('Week 4:', w4)
print('---------------')
print('TOTAL:', monthly_expenses)