import random

rolls = 4
special = False
print(f'Dice rolled: {rolls}')
for x in range(rolls):
    roll = random.randint(1, 6)
    if roll == 1 or roll == 6:
        special = True
print(f'Special rolled? : {special}')