"""
Sistema de gestión de empleados con registro de acciones.

Este módulo implementa un sistema simple para agregar empleados y registrar
todas las acciones realizadas en un archivo de log con timestamps.
"""

from datetime import datetime
from pathlib import Path

# Lista global para almacenar los empleados
employee_list = []

# Configurar la ruta para guardar los archivos de log
actions_path = Path(__file__).parent.parent / 'CSVs'
actions_path.mkdir(parents=True, exist_ok=True)  # Crear directorio si no existe

def log_action(func):
    """
    Decorador que registra las acciones de las funciones en un archivo de log.

    Este decorador envuelve una función y registra cada vez que se ejecuta,
    guardando el nombre de la función y la fecha/hora en message.txt.

    Args:
        func: La función a decorar.

    Returns:
        wrapper: La función envuelta con funcionalidad de logging.
    """
    def wrapper(*args, **kwargs):
        print("Iniciando accion...")

        # Registrar la acción en el archivo de log
        with open(actions_path / 'message.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"Accion: {func.__name__} - Fecha y hora: {datetime.now()}\n")

        # Ejecutar la función original y guardar el resultado
        result = func(*args, **kwargs)
        print("Accion finalizada.")
        return result
    return wrapper

@log_action
def add_employee(employee_list, name, position):
    """
    Agrega un nuevo empleado a la lista de empleados.

    Esta función crea un diccionario con la información del empleado
    y lo añade a la lista proporcionada.

    Args:
        employee_list (list): La lista donde se agregará el empleado.
        name (str): El nombre del empleado.
        position (str): El cargo o posición del empleado.

    Returns:
        list: La lista actualizada de empleados.
    """
    # Crear diccionario con la información del empleado
    employee = {
        'name': name,
        'position': position
    }
    print(f"Empleado agregado: {name} ({position})")

    # Agregar el empleado a la lista
    employee_list.append(employee)
    return employee_list


# Ejemplo de uso: agregar un empleado a la lista
add_employee(employee_list, 'Juan Perez', 'Developer')