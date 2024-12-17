grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

pgrades = list(filter(lambda x : x > 2.0, grades))
pgradesavg = sum(pgrades) / len(pgrades)

print (pgradesavg)