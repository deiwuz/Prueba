from typing import Dict


#Decordador para comprobar el rol de un empleado
def check_access(required_role: str):
    def decorator(func):
        def wrapper(employee: Dict[str, str | int]):
            if employee.get('role') == required_role:
                print(f"Acceso concedido al empleado {employee['name']} con rol {employee['role']}")
                return func(employee)
            else:
                print(f"El empleado {employee['name']} no tiene permisos para ejecutar esta accion. Se requiere empleado con rol {required_role}.")
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee: Dict[str, str | int]):
        print(f"Iniciando registro de accion para {employee['name']}")
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee: Dict[str, str | int]) -> None:
    """Deletes an employee from the database."""
    # Function implementation goes here
    print(f"El empleado {employee['name']} con id {employee['id']}, ha sido eliminado")

admin = {'name': 'Alice', 'id': 1, 'role': 'admin'}
employee = {'name': 'Bob', 'id': 2, 'role': 'user'}

delete_employee(admin)  # Should allow access and log action
delete_employee(employee)  # Should deny access