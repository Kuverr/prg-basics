person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])

for key, data in person.items():
    print(f'{key}: {data}')

person["surname"] = "Nowak"

person["married"] = False

person["gender"] = "male"

zxc = []
for i in person["hobby"]:
    zxc.append(i)
zxc.append("bicycle")
person["hobby"] = zxc

person["phone"]["work"] = "313131444"

for key, data in person.items():
    print(f'{key}: {data}')