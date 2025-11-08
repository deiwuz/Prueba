import json

file_path = 'C:/Users/Esteban/Documents/Aprendizaje/Products/products.json'

#Lectura del archivo
with open(file_path, mode='r') as file:
    products = json.load(file)
    pass

#Mostrar el contenido
for product in products:
    #print(product)
    print(f"product: {product['name']}, Price: {product['price']}, Category: {product['category']}")

new_product = {
    "name": "Wireless Charger",
    "price": 1750,
    "quantity": 8,
    "brand": "Sony",
    "category": "Accesories",
    "entry_date": "2025-09-29"
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)

for product in products:
    #print(product)
    print(f"product: {product['name']}, Price: {product['price']}, Category: {product['category']}")