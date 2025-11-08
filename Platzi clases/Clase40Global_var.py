x = 5 #Variable global

def modify_global():
    global x 
    x += 3
    print(f'La variable global modificada es {x}')

print(f'La variable global es {x}')
modify_global()
print(f'La variable global es {x}')