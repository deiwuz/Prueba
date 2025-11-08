print ("Bienvenido a tu calculadora\n\nEstas son las opciones:")

def calculator():
    
    def add(a, b):
        return a+b

    def substract(a, b):
        return a-b

    def multiply(a, b):
        return a*b

    def divide(a, b):
        return a/b
    
    while True:
    
        try:
            option = int(input("1. suma\n2. resta\n3. multiplicacion\n4. division\n5. salir\n\nSelecciona que opcion deseas:"))
        except ValueError:
            print("\nDebes seleccionar una de las opciones\n")
            continue

        if option == 5:
            print("\nEstas saliendo de tu calculadora\n")
            break

        if option not in [1,2,3,4,5]:
            print("\nDebes elegir una de las opciones\n")
            continue

        try:
            num1 = float(input("Cual es el primer numero?\n:"))
            num2 = float(input("Cual es el segundo numero?\n:"))
        except ValueError:
            print("Debes escribir un Numero")
            continue
    
        if option == 1:
            print(f"\nel resultado de la suma es:\n{add(num1, num2)}")
        elif option == 2:
            print(f"\nel resultado de la resta es:\n{substract(num1, num2)}")
        elif option == 3:
            print(f"\nel resultado de la multiplicacion es:\n{multiply(num1, num2)}")
        elif option == 4:
            try:
                print(f"\nel resultado de la division es:\n{divide(num1, num2)}")
            except ZeroDivisionError:
                print("\nNo se puede dividir entre cero\n")

calculator()