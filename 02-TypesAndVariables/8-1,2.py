###
# Calculation of circle area and circumference 
#
import math
# determine radius and PI values
r = float(input('Enter radius: '))
pi = round(math.pi, 2)
# calculate area 
area = pi * r ** 2
# calculate circumference 
circumference = 2 * pi * r
# print results
print(f'Radius: {r}')
print(f'Area: {area}')
print(f'Circumference: {circumference}')