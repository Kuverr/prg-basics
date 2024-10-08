import math

a = float(input('Enter your height in meters: '))
d = 3.57 * math.sqrt(a)

print('Distance to horizon while on the beach: ', d)

h = 20 + a
d = 3.57 * math.sqrt(h)

print('Distance to horizon while on the beach: ', d)
