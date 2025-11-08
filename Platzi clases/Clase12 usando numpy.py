import numpy as np
import copy
separacion = "----------------"
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(a[2][1])
print(a[1][2])

matrix = np.array([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])

print (matrix)
print(matrix[0][2])

matrix2 = np.array([[[1,2],[3, 4]],
                    [[5,6], [7, 8]],
                    [[0, 10], [11, 12]]])

#print("original\n:", matrix2[0][1][0])

numbers2 = (1,2,3,4,5,[10,12])
b = copy.deepcopy(numbers2[:]) #primera copia antes de cualquier modificacion
numbers2[5][0] = 30 #modificacion 1 cambia el 10 por 30
c = copy.deepcopy(numbers2[:]) #segunda copia luego de la primera modificacion
print("modificacion1\n:",numbers2) #print con la modificacion 1 que cambia el 10 por el 30
numbers2[5][1] = 15 #segunda modificacion que cambiar el 12 por el 15
print("modificacion2\n:",numbers2) #print de la segunda modificacion que cambia el 12 por el 15
print("primera copia profunda\n,:", b) # primera copia profunda
print("segunda copia profunda\n,:", c) # segunda copia profunda
print(separacion) # separacion
matrix2[1][1][1] = 23
print(matrix2)
print(separacion) # separacion
matrix2[1][1] = np.delete(matrix2[1][1], 1)
print(matrix2)
print(separacion) # separacion
matrix2[2][1][0] = 9
print(matrix2)
print(separacion) # separacion
matrix2[2][0]= np.delete(matrix2[2][0], 0)
print(matrix2)

