a = [1, 2, 3, 4, 5,
     6, 7, 8 , 9, 10]
b = a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
c = a[:]
print(c)
print(id(c))
a.append(12)
print("separaci")
print(a)
print(b)
print(c)
