###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# take input in Celsius, conver from string to float
c = float(input('Enter temperature in degrees Celsius: '))
# convert Celsius to Kelvin and Fahrenheit with corresponding formulas
k = c + 273.15
f = (9/5) * c + 32
# print results
print(f'{c} degrees celsius is {k} in Kelvin and {f} in Fahrenheit')