a = 100

def local_function():
    x = 10 #variable local
    print(f'El valor de la variable es {x}')

def show_global():
    print(f'El valor de la variable global es {a}')

local_function()
#print(x) #Genera error
show_global()
print(a)