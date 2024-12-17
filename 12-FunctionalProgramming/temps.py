temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

postemp = list(map(lambda y : y[0], list(filter(lambda x : x[1] > 0, temps.items()))))

print (postemp)