import csv

new_product = {
    'name': 'Lentes',
    'price': 700,
    'quantity': 6,
    'brand': 'Aquavue',
    'category': 'Health',
    'entry_date': '2025-09-25',
    'total_value': 4200
}

with open ('C:/Users/Esteban/Documents/Nueva carpeta/products_updated.csv', mode='a', newline='') as file:
    #file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_writer.writerow(new_product)