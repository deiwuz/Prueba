
# Leer archivo linea por linea
with open('C:/Users/Esteban/Desktop/caperucita.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Leer todas las linea en una lista
with open('C:/Users/Esteban/Desktop/caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Escribir en un archivo ya creado
with open('C:/Users/Esteban/Desktop/caperucita.txt', 'a') as file:
    file.write("\n\nHola")

# Contar las linea de un archivo

with open ('C:/Users/Esteban/Desktop/caperucita.txt', 'a') as file:
    file.write('\n\nHola')

with open ('C:/Users/Esteban/Desktop/caperucita.txt', 'r') as file:
    Lines = file.readlines()
    print(len(Lines))