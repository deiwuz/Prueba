def gen_numbers(limit, tipo):
    if tipo == 'par':
        a = 0
    elif tipo == 'impar':
        a = 1
    else:
        raise ValueError("los tipos deben ser 'par' o 'impar'")
    
    while a < limit+1:
        yield a
        a += 2

while True:
    opcion =input('\nEscribe un numero limite para continuar o \'salir\' para terminar:\n')


    if opcion == 'salir':
        print("programa terminado")
        break

    try:
        limit = int(opcion)
    except ValueError:
        print('Debes ingresar un numero limite o "salir" para terminar.')
        continue

    while True:

            tipo = input("¿Quieres ver números 'par' o 'impar'?\n").strip().lower()
            if tipo in ['par', 'impar']:
                break
            else:
                print('Por favor ingresa solo \'par\' or \'impar\'')

    if tipo in ['par', 'impar']:
        print(f'los numeros {tipo}es hasta {limit} son:')
        print(','.join(str(n)for n in gen_numbers(limit, tipo)))





