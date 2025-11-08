name = input("ingrese su nombre:")
print(name)
age = int(input("ingrese su edad:")) 
print(age)
print(type(age))
print(type(name))

# Revised code with improvements

name = input("Enter your name: ")
print(f"Your name is: {name}")
try:
    age = int(input("Enter your age: "))
    print(f"Your age is: {age}")
    print(f"Type of age: {type(age)}")
except ValueError:
    print("Please enter a valid number for age.")
print(f"Type of name: {type(name)}")

# Nota sobre try y except:
# try:
# El código dentro de este bloque se ejecuta normalmente. Si todo sale bien, continúa.
#
# except ValueError:
# Si ocurre un error del tipo ValueError (por ejemplo, si el usuario escribe letras en vez de un número), el programa no se detiene.
# En vez de eso, ejecuta el código dentro de except y muestra el mensaje:
# "Please enter a valid number for age."