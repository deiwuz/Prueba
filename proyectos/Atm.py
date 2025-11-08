import random
print("/////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("Bienvenido a tu cajero automatico")
print("Puedes escribir \"salir\" cuando quieras terminar el programa\n")

bank ={
    1: ["Davivienda"],
    2: ["Banco de bogota"],
    3: ["Bancolombia"]
}

operaciones = {
     1: ["deposito", lambda a,b: a+b],
     2: ["retiro", lambda a,b: a-b],
     3: ["consulta", lambda a: a]
}


def Atm1():
    
    balance = random.uniform(0, 100)

    while True:
            eleccion_banco = int(input("1.Davivienda\n2.Banco de bogota\n3.Bancolombia\n4.Salir\nSelecciona una opcion: "))
            if eleccion_banco == 4:
                print("Se ha finalizado el programa")
                return
            try:
                if eleccion_banco in bank:
                    print(f"\nHas seleccionado {bank[eleccion_banco][0]}.\n")
                    break
                elif eleccion_banco not in bank:
                    raise ValueError
            except ValueError: print("La eleccion es invalida")
    
    while True:
        try:
            eleccion_operacion = int(input("1.Depositar\n2.Retirar\n3.Consulta de saldo\n4.Salir\nSelecciona la operaccion que quieres realizar: "))
            if eleccion_operacion == 4:
                print("Se ha finalizado el programa")
                return
            elif eleccion_operacion not in operaciones:
                raise ValueError
            elif eleccion_operacion==1:
                try:
                    deposito=float(input("Valor del deposito: "))
                    a, b = float(balance), (deposito)
                    if deposito <= 0:
                        raise ValueError
                    balance = operaciones[eleccion_operacion][1](a, b)
                    print (f"Has depositado {deposito} correctamente, tu nuevo balance es: {(balance):.2f}")
                except ValueError: print ("El valor a depositar debe ser un numero positivo")
            elif eleccion_operacion==2:
                try:
                    retiro=float(input("Valor del retiro: "))
                    a, b =float(balance), (retiro)
                    if retiro <= 0:
                        raise ValueError
                    elif retiro > balance:
                        print("Fondos insuficientes")
                        continue
                    balance = operaciones[eleccion_operacion][1](a, b)
                    print (f"Has retirado {retiro} correctamente, tu nuevo balance es: {(balance):.2f}")
                except ValueError: print ("El valor a retirar debe ser un numero positivo")
            elif eleccion_operacion==3:
                print(f"tu saldo actual es de: {(balance):.2f}")
        except ValueError: print("La eleccion es invalida")
    
    

Atm1()