class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("La edad no puede ser negativa")
        self._age = value


p = Person("Ana", 25)
print(p.age)   # ✅ Se usa como atributo, pero llama al método
p.age = 30     # ✅ setter modifica _age
print(p.age)
p.age = -5    # ❌ Lanza ValueError
print(p.age)