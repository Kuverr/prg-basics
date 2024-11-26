countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":50000000},
    {"name":"France", "population":45000000},
    {"name":"Sweden", "population":21000000},
    {"name":"Italy", "population":30000000}
]

for i in countries:
    for a,b in i.items():
        print(f'{a}: {b}')