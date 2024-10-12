import math

cicrumference = int(input('Enter tree circumference: '))
diameter = round(cicrumference / math.pi)
canBeCut = diameter >= 50
print(f'Tree diameter: {diameter}')
print(f'Can the tree be cut down? : {canBeCut}')