employee_list = []
from datetime import datetime
from pathlib import Path

actions_path = Path(__file__).parent.parent / 'CSVs'
actions_path.mkdir(parents=True, exist_ok=True)

def log_action(func):
    def wrapper(*args, **kwargs):
        print("Iniciando accion...")
        with open(actions_path / 'message.txt', 'a', newline="", encoding='utf-8') as log_file:
            log_file.write(f"Accion: {func.__name__} - Fecha y hora: {datetime.now()}\n")
        result = func(*args, **kwargs)
        print("Accion finalizada.")
        return result
    return wrapper

@log_action
def add_employee(employee_list, name, position):
    """Adds a new employee to the employee list."""
    employee = {
        'name': name,
        'position': position
    }
    print(f"Empleado agregado: {name} ({position})")
    employee_list.append(employee)
    return employee_list

add_employee(employee_list, 'Juan Perez', 'Developer')