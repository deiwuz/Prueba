import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y mi edad es {self.age}")

persona1= Person("Ana", 55)
persona2= Person("freddy", 50)


class Bankaccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
            try:
                if not self.is_active:
                    print("No se puede depositar, Cuenta inactiva")
                    return
                
                if amount <= 0:
                    raise ValueError("El valor a depositar debe ser un numero positivo")
                self.balance += amount
                print(f"\nSe ha depositado {amount}, Saldo actual {self.balance}")

            except ValueError as e:
                print(e)
    
    def withdraw(self, amount):
        try:
            if not self.is_active:
                print("No se puede retirar. Cuenta inactiva")
                return
            
            if amount <=0:
                raise ValueError("El Valor a retirar debe ser un numero positivo")

            if amount <= self.balance:
                self.balance -= amount
                print(f"\nSe han retirado {amount}, Saldo actual {self.balance}")
            else:
                print("Saldo insuficiente")
        except ValueError as e:
            print(e)

    def deactivation(self):
        self.is_active = False
        print("La cuenta se ha desactivado")
    
    def activation(self):
        self.is_active = True
        print("La cuenta se ha activado")


def Atm():
    print("///////////////////////////////////////////////////////////////////////////////////")
    print("Bienvenido a tu cajero automatico")
    print("Puedes escribir \"salir\" cuando quieras terminar.\n")

    Banks = {1: ["Davivienda"],
             2: ["Banco de bogota"],
             3: ["Bancolombia"]
             }
    
    Users ={1: Bankaccount("Esteban", 1500),
            2: Bankaccount("Karol", 1000),
            3: Bankaccount("Ana", 2000)
            }
    
# Eleccion de banco    
    while True:
        Bank = input("1. Davivienda\n2. Banco de bogota\n3. Bancolombia\n4. Salir\n\nSelecciona una opcion: ").lower()
        if Bank == "4" or Bank == "salir":
            print("Se ha terminado el programa")
            return

        try:
            Eleccion_banco = int(Bank)
            if Eleccion_banco in Banks:
                print(f"Has seleccionado {Banks[Eleccion_banco][0]}\n")
                break
            else:
                print("No has selecciona una opcion de banco valida")
        except ValueError: print("Valor incorrecto")

# Eleccion de  cuenta

    while True:
        Usuario = input("Introduce tu numero de cedula: ").lower()
        if Usuario == "salir":
            print("Se ha terminado el programa")
            return
        try:
            Eleccion_usuario = int(Usuario)
            if Eleccion_usuario in Users:
                print(f"\nHola {Users[Eleccion_usuario].account_holder}, Bienvenido a tu cuenta del banco {Banks[Eleccion_banco][0]}")
                break
            elif Eleccion_usuario not in Users:
                print(f"El numero de cedula introducido es incorrecto o no tiene una cuenta con el banco {Banks[Eleccion_banco][0]}")
                continue
        except ValueError: print("Numero de cedula invalido")

# Operaciones

    while True:
        Operacion = input("1.Deposito\n2.Retiro\n3.Desactivar cuenta\n4.Activar cuenta\n5.Salir\n\nSelecciona una operacion: ").lower()
        if Operacion in ("salir", "5"):
            print("Se ha terminado el programa")
            return
        
        Eleccion_operacion = int(Operacion)
        if Eleccion_operacion not in (1,2,3,4):
            print("Has selecciona una operacion invalida")
        if Eleccion_operacion == 1:
            try:
                amount = float(input("\nValor del deposito: "))
                Users[Eleccion_usuario].deposit(amount)
            except ValueError: print("El valor a depositar debe ser un numero positivo")
        if Eleccion_operacion ==2:
            try:
                amount = float(input("\nValor del retiro: "))
                Users[Eleccion_usuario].withdraw(amount)
            except ValueError: print("El valor a retirar debe ser un numero positivo")
        if Eleccion_operacion ==3:
            Users[Eleccion_usuario].deactivation()
        if Eleccion_operacion ==4:
            Users[Eleccion_usuario].activation()


Atm()