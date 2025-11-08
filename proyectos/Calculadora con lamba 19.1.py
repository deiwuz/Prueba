print('Bienvenido a tu calculadora')
def Cal():
    opt={
        1: ("Suma", lambda a, b: a+b),
        2: ("Resta", lambda a, b: a-b),
        3: ("Multiplicacion", lambda a, b: a*b),
        4: ("Division", lambda a, b: a/b)
    }

    while True:
        try:
            op = int(input('\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Salir\nSelecciona una opcion: '))
            if op == 5:
                break
            if op not in opt: raise ValueError
            a, b = float(input("Selecciona el primer numero: ")), float(input("Selecciona el segundo numero: "))
            try: print(f"EL resultado de {opt[op][0]} es {opt[op][1](a, b)}")
            except ZeroDivisionError: print("No se puede dividir entre cero")
        except ValueError: print("Valor o opcion incorrecta")

Cal()