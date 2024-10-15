###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
msg = ''
for i in range(1,11):
    frac = round(1 / i, 3)
    i = str(i)
    msg += f'1/{i} = {frac}\n'
print(msg)