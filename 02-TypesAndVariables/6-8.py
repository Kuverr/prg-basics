###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
second = input('Enter second letter: ')
first_code = ord(first)
second_code = ord(second)
if first_code == second_code:
    n = 0
else:
    n = abs(first_code - second_code) - 1
print(f'Between {first} and {second} is {n} letters')