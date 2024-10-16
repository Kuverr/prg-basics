###
# Sums numbers entered by user
#
total_sum = 0
number_amount = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    number_amount += 1
    total_sum += number


print(f"The total sum of the numbers is: {total_sum}")
print(f'Arithmetic mean of numbers is: {total_sum/number_amount}')