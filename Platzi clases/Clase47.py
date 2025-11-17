class Juguete:
    def __init__(self, nombre):
        self.nombre = nombre

    def __add__(self, otro_juguete):
        return Juguete(self.nombre + " y " + otro_juguete.nombre)

# Crear dos juguetes
juguete1 = Juguete("Carro")
juguete2 = Juguete("Avión")

# Usar el método mágico __add__ para "sumar" los juguetes
juguete3 = juguete1 + juguete2

print(juguete3.nombre)  # Salida: Carro y Avión

class Vector:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def __add__(self, other):

        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):

        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)

v2 = Vector(1, 5)

print(v1 + v2) # Salida: Vector(3, 8)

print(str(v1)) # Salida: Vector(2, 3)