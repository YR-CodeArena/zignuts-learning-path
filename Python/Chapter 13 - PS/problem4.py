fun = lambda x: x%5 == 0

lst = [1, 5, 12, 154, 15, 90]
f = list(filter(fun, lst))
print(f)
