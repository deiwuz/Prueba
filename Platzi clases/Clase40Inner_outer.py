x = 'global' #Variable global

#funcion externa
def outer_function():
    x = 'enclosing'

    #Funcion interna
    def inner_funcion():
        x = 'local' #Varibale local
        print(x)
    
    inner_funcion()
    print(x)

outer_function()
print(x)
