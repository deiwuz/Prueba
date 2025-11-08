separacion = "========================================================================================================"
print(separacion)
to_do = ["terminar mi dia laboral",
            "hacer ejercicio",
            "estudiar python",]
print(to_do)
print(type(to_do))
print(separacion)
#En Python, los corchetes [] se usan para crear listas, que son colecciones ordenadas y modificables de elementos.
#los paréntesis () se usan para crear tuplas, que son colecciones ordenadas pero no modificables. # type: ignore

#Una tupla en Python es una colección ordenada de elementos, similar a una lista, 
#pero inmutable (no se puede modificar después de crearla).

my_tuple = ("lunes", "martes", "miércoles")
print(my_tuple)           # Muestra la tupla completa
print(type(my_tuple))     # <class 'tuple'>
print(my_tuple[1])        # Accede al segundo elemento ("martes")
print(separacion)
# Listas

numbers = [1, 2, 3, 4, "cuatro"]
print(numbers)
print(type(numbers))

mix = [1, "tres", 2.0, False, [1, 2, 3, 4, "siete"]]

print(mix)
print(type(mix))
print(mix[3])        # Accede al quinto cuarto (la lista interna)
print(mix[4][4])     # Accede al tercer elemento "False" y accede al quinto elemento de la lista interna "siete"
print(mix[0:4])      # Accede a una porción de la lista desde el índice 0 hasta el 2 (excluye el 4)
print("Primer elemento:", mix[0]) # Accede al primer elemento de la lista
print("Último elemento:", mix[-1])  # Accede al último elemento de la lista
string = "Hola, mundo"

print("primer elemento:", string[0])
print("ultimo elemento:", string[-1])
print(mix[:5])
print(mix[0:])
# --------------------------
print(separacion)
# ---------------------------
print(mix)
mix.append("quiza no es tan dificil")
print(mix)
print(mix[0:])
print(mix[0:-1])
print(mix[5])
print(mix[4][2])
print(mix[0])
print(separacion)
mix.insert(0, "elemento insertado")
print(mix)
mix.pop(-1)
print(mix)
print(len(mix))
print(mix.index((2.0)))
print(mix.index([1, 2, 3, 4, "siete"]))
# separacion
print(separacion)
# separacion
numeros = [1, 200, 3000, 120, 10000]
print(numeros)
print("Numero mayor:", max(numeros))
print("Numero menor:", min(numeros))
print("suma de todos los numeros", sum(numeros))
del numeros[4]
print(numeros)
del numeros[0:1]
del numeros[3:4]
print(numeros)