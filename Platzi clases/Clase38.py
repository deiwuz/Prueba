class Calculator: #Clases inician con mayuscula
    def add_number(self, first_number, second_number): #funciones inician con minuscula y sus espacios son _
        result = first_number + second_number# luego de cada "," o "+" se utiliza un espacio " "
        return result

calc = Calculator()

print(calc.add_number(5, 3)) #cada linea de codigo tiene un maximo de 79 caracteres