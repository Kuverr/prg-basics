numbers = [2,4,6,3,7,5]

evensum = sum(list(filter(lambda x : x % 2 == 0, numbers)))

print (evensum)
