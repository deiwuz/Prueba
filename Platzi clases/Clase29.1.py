class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

person1 = Person("Esteban", 21)

print(person1)          # Usa __str__ → Esteban, 21 años
print(repr(person1))    # Usa __repr__ → Person(name=Esteban, age=21)

# Cuando inspeccionas una lista:
print([person1])        # Usa __repr__ → [Person(name=Esteban, age=21)]