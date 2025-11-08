import random

print("Hola, Bienvenido a el juego de adivinanzas")
print("Puedes escribir \"Salir\" cuando quieras terminar el programa")


def juego():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            Ayuda = input("Sabes como se juega?\n: ").lower()
            if Ayuda == "salir":
                print("El juego ha terminado")
                return
            elif Ayuda == "si":
                print("Perfecto podemos continuar")
                break
            elif Ayuda == "no":
                print("El sistema generara un numero aleatorio de 1 a 100, debes adivinar este numero en la menor cantidad de intentos!")
                break
            else:
                raise ValueError
        except ValueError: print('Las opciones deben ser "Si" o "No"')
    
    while True:
        Eleccion = input("Elige un numero entre 1 y 100\n: ")   
        if Eleccion.lower() == "salir":
            print(f"El juego ha terminado, el numero era: {numero_secreto}")
            return

        try:
            Eleccion = int(Eleccion)
            intentos += 1
            if Eleccion < numero_secreto:
                print("Muy bajo, intenta de nuevo")
            elif Eleccion > numero_secreto:
                print("Muy alto, intenta de nuevo")
            elif Eleccion == numero_secreto:
                print (f"!Felicidades! Lo lograste en {intentos} intentos")
                break
        except ValueError: print("El numero ingresado debe ser un valor entero positivo")

    while True:
        try:
            otra = input("Deseas volver a jugar? (Si/no)\n: ").lower()
            if otra == "si":
                return juego()
            elif otra == "no":
                print("El juego ha terminado")
                return
            else:
                raise ValueError
        except ValueError: print("Debes seleccionar 'si' o 'no'\n: ")
            
juego()
        


