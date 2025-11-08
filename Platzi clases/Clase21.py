#n=(int(input('Ingrese el primer valor: ')))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#print(f"El resultado del factorial de {n} es igual a: {factorial(n)}")

def fibonacci(v):
    if v < 0:
        raise ValueError
    elif v == 0:
        return 0
    elif v == 1:
        return 1
    else:
        return fibonacci(v-1) + fibonacci(v-2)

def sec():
    print('Puede escribir "Salir" para terminar el programa')
    while True:
        entrada = input("\nIngrese la secuencia de fibonacci que desea encontrar:")
        if entrada.lower() == "salir":
            break
        try:
            v = int(entrada)
            print(f"El valor de la secuencia {v} de fibonacci es: {fibonacci(v)}")
        except ValueError: print("Debe ser un numero entero positivo")

sec()


