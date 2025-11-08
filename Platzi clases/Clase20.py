opt={
        1: ("Suma", lambda a, b: a+b),
        2: ("Resta", lambda a, b: a+-b),
        3: ("Multiplicacion", lambda a, b: a*b),
        4: ("Division", lambda a, b: a/b)
    }

# cuadrados

Numeros = range(11)
Numeros_cuadrados = list(map(lambda x: x**2, Numeros))
print(Numeros_cuadrados)

# pares

Numeros= range(101)
Numeros_pares = list(filter(lambda x: x%2 == 0, Numeros))
print (Numeros_pares)