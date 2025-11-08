import csv
import json


products = []

file_path = 'C:/Users/Esteban/Documents/Aprendizaje/Products/products.json'
new_file_path_csv = 'C:/Users/Esteban/Documents/Aprendizaje/Products/json to csv.csv'

with open(file_path, mode='r', encoding='utf-8', newline='') as file:
    products = json.load(file)

if isinstance (products, dict):
    products = [products]

with open(new_file_path_csv, mode='w', encoding='utf-8') as csv_file:
    fieldnames = products[0].keys()
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerows(products)