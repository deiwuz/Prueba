import csv

file_path = 'C:/Users/Esteban/Documents/Nueva carpeta/products.csv'
updated_file_path = 'C:/Users/Esteban/Documents/Nueva carpeta/products_updated.csv'



with open(file_path, mode= 'r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode= 'w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() # Escribir encabezado

        for row in csv_reader:
            row['total_value'] = float(row['price']) * float(row['quantity'])
            csv_writer.writerow(row)