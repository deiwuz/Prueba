import csv
import json

file_path = 'C:/Users/Esteban/Documents/Aprendizaje/Products/products.csv'
new_file_path_json = 'C:/Users/Esteban/Documents/Aprendizaje/Products/products.json'

products = []


with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        products.append(line)

with open(new_file_path_json, mode='w') as file:
    json.dump(products, file, indent=4)

