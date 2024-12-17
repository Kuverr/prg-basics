emp = [
    "SMITH Lucy",
    "JONES Janet",
    "LEE Jerry",
    "JACKSON Peter",
    "JOHNSON Rick",
    "LEWIS Terry",
    "CLARKE Robin"
]

jsname = list(filter(lambda x : x.split(" ")[0][0] == 'J', emp))

print(jsname)