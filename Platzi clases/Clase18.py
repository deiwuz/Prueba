sep = "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
square = [x**2 for x in range(1,10)]
#print(f"cuadrados son: {square}")
#print(sep)

celsius = list(range(20,30))
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
#print(f"Temperatura en F:\n{' '.join(str(x) for x in fahrenheit)}")
#print(f"Temperatura en C:\n{' '.join(str(x) for x in celsius)}")

#print(sep)

evens = [x for x in range(0,20+1) if x%2 ==0]
#print(evens)

##print(sep)

matrix = [[10,20,30],
          [40,50,60],
          [70,80,90]]

transposed = [[fila[columna] for fila in matrix] for columna in range(len(matrix[0]))]

print(transposed)