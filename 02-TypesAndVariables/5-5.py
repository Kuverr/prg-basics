price = float(input('Insert price: '))
discount = int(input('Discount %: '))

new_price = round(price * (1 - discount / 100), 2)
reduction = round(price - new_price, 2)

print(f'Price with discount: {new_price} \nReduction: {reduction}')