###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = bool(int(input("Is bonus? (0/1): ")))
if is_bonus:
    bonus = 0.01 * int(input("Insert bonus %: "))

if is_bonus:
    total_salary = basic_salary * (1 + bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')