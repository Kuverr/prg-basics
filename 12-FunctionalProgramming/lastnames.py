emps = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

lnamescapt = list(list(map(lambda x : f'{x[0].upper()}, {x[1]}', emps)))

print (lnamescapt)