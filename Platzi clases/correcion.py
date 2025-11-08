import csv
import json

file_path = 'C:/Users/Esteban/Documents/Aprendizaje/Products/products.json'
new_file_path_csv = 'C:/Users/Esteban/Documents/Aprendizaje/Products/json_to_csv.csv'

# Leer el JSON
with open(file_path, mode="r", encoding="utf-8") as file:
    productos = json.load(file)

# Si el JSON contiene un solo objeto, lo envolvemos en una lista
if isinstance(productos, dict):
    productos = [productos]

# Crear el CSV
with open(new_file_path_csv, mode='w', newline='', encoding="utf-8") as csv_file:
    # Usar las llaves del primer diccionario como encabezados
    fieldnames = productos[0].keys()
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerows(productos)

print("Conversión completada con éxito ✅")
