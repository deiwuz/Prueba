import statistics
import csv



monthly_sales_path_file = 'C:/Users/Esteban/Documents/Aprendizaje/clase33.csv'
monthly_sales = {}
with open(monthly_sales_path_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())

#Hallar la media

mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales:.02f}")

#Hallar la mediana

median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales:.02f}")

#Hallar la moda solo halla 1

mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales:.02f}")

#Hallar todas las modas si hay mas de 1

mode_sales = statistics.multimode(sales)
print(f"Las moda son: {mode_sales}")

#Desviacion estandar

stdev_sales = statistics.stdev(sales)
print(f"La desviacion estandar es: {stdev_sales:.02f}")

#Varianza

variance_sales = statistics.variance(sales)
print(f"La varianza es: {variance_sales:.02f}")

#Dato maximo

max_sales = max(sales)
max_months = [month for month, value in monthly_sales.items() if value == max_sales]
print(f"las ventas maximas alcanzadas fueron de {max_sales} en los siguientes meses: {", ".join(max_months)}")

#dato minimo

min_sales = min(sales)
min_months = [month for month, value in monthly_sales.items() if value == min_sales]
print(f"las ventas minimas alcanzadas fueron de {min_sales} en los siguientes meses: {", ".join(min_months)}")

#rango de ventas

range_sales = max_sales - min_sales
print(range_sales)



