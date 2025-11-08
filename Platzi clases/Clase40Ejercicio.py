employees = [
    {"name": "Esteban", "age": 25, "salary": 3500},
    {"name": "Laura", "age": 30, "salary": 4200},
    {"name": "Carlos", "age": 28, "salary": 3900},
    {"name": "Sofía", "age": 35, "salary": 5000}
]


def empleados():
    """
    Filtra una lista de empleados con sueldos superiores a 4000.

    Utiliza la lista global 'employees' y muestra los resultados por consola.
    """

    empleados = employees
    empleados_con_mayor_sueldo = []
    def mayor_sueldo():
        """
        Filtra los empleados con mayor sueldo y los agrega
        a la lista empleados_con_mayor_sueldo.
        """

        for empleado in empleados:
            if empleado['salary'] > 4000:
                empleados_con_mayor_sueldo.append(empleado)
    mayor_sueldo()

    #Imprime la lista de empleados con mayor sueldo     
    print("Los empleados con un sueldo superior a 4000 son:")
    for e in empleados_con_mayor_sueldo:
        print(f"{e['name']}, salario: {e['salary']}")
          
empleados()

