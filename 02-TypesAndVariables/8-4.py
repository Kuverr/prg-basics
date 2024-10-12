###
# A program that prints your height both in cm and in feet and inches.
#
cm = 185
# 1inch is 2.54cm approx
feet = round(cm // (2.54 * 12))
inches = round(cm % (2.54 * 12) / 2.54, 2)
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')