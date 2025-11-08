import csv

products = []

# Leer un archivo csv

with open('C:/Users/Esteban/Documents/Nueva carpeta/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        print(line)

# Por cada linea en el archivo Csv imprimir nombre, unidades disponibles y precio

with open('C:/Users/Esteban/Documents/Nueva carpeta/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        print(f"Producto: {line['name']}/unidades disponibles: {line['quantity']}/precio: {line['price']}")



