ar20 = []
i = 1
while i <= 20:
    ar20.append(i)
    i+=1
print (ar20)

pw3rd = list(map(lambda x : x**3, ar20))

print (pw3rd)

div2n3 = list(filter(lambda x : x % 2 == 0 and x % 3 == 0, ar20))

print (div2n3)