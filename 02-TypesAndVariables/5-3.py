###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

volume = a * b * c
area = 2*(a*b + a*c + b*c)

print(f'Cuboid sides: a={a}, b={b}, c={c}')
print(f'Cuboid surface area: {area}')
print(f'Cuboid volume: {volume}')