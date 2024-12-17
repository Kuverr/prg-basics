def test(x):
    return lambda y : x + y

print(test(10)(5))
test10 = test(10)
print(test10(5))