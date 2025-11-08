import numpy as np
import copy
separacion = "--------------------------------------------------------------------------------------------------------------------------------"
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(a)

matrix =[[[5,6],[7,8]],
         [[43,51],[12,76]]]
print(matrix[0][1][0])

numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers))
print(numbers[2])
#numbers[2] = 24


chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print(separacion)
chess_board[7][1] = 0  # Casilla original del caballo ahora está vacía
chess_board[5][2] = 'N'  # Nueva posición del caballo
chess_board[1][2] = 0
chess_board[2][2] = 'p'
chess_board[0][3] = '0'
chess_board[5][0] = 'q'


b = '\n'.join(' '.join(str(x) for x in fila) for fila in chess_board)

print(b)

print(separacion)

image = [
    [255, 0, 0, 0, 255],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 0, 0,],
    [0, 255, 0, 255, 0],
    [255, 0, 0, 0, 255]
]

print(image)

print(separacion)
for fila in image:
    print(*fila)
print(separacion)
z = '\n'.join(' '.join(str(pixel) for pixel in fila) for fila in image)

print(z)



semana = [
    ['levantarme', 'apagar la alarma', 'banarme'],
    ['salir', 'llegar', '1'],
    ['salir', 'volver', 'gimnasio'],
    ['estudiar']
]

dia = '\n'.join(' '.join(z for z in actividades)for actividades in semana)


print(dia)