sep = '////////////////////////////////////////////////////////'
# Ejemplo de iterador
#Crea una lista

my_list = [1,2,3,4]

#Obtener el iterador

my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print(sep)


#iterar en cadenas
#creando la cadena
text = 'Hola Mundo'
#creando el iterador
iter_text = iter(text)
#iterar en la cadena

for char in iter_text:
    print(char)

print(sep)

#crear un iterador para los numeros impares
#Limite
limit = 10

#crear iterador
odd_itter= iter(range(1,limit+2,2))

#usar iterador

for num in odd_itter:
    print(num)

print(sep)

#generador
def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)
print(sep)
#Fibonacci

def fib(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a, b = b, a+b

for val in fib(1):
    print(val)

print(sep)

