sep = "/////////////////////////////////////////////////////////"


numbers = {1:"uno", 2:"dos", 3:"tres"}

print(numbers[3])

information = {"nombre":"john",
             "altura":"1.70",
             "edad":"veinti uno"}



print(sep)
print(information)

print(sep)
#del information["nombre"] elimina un llave
print(information)

print(sep)
keys = information.keys()
print(keys)

print(sep)
print(type(keys))

print(sep)
values = information.values()
print(values)

print(sep)
pairs = information.items()
print(information)

print(sep)
Contacts = {"Esteban" :{"Nombre": "Esteban",
                "Numero": "3236596664",
                "Emergencia": "Si",
                "secundario": "3124950817"},
        "Mama":{"Nombre": "Mama",
                "Numero": "3124950817",
                "Emergencia": "No",
                "secundario": "3"}
}

Lista = "\n".join(' '.join(str(valores)for valores in contacto.values())for contacto in Contacts.values())

print(Lista)