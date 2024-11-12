###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[3])
print('Sum', arr[0] + arr[-1])
print('Mid', arr[len(arr) // 2])
all = ''
for i in arr:
    all += str(i) + ' '
print('All:', all)