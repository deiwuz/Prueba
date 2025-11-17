from typing import TypedDict
from pathlib import Path
import csv

class Employee(TypedDict):
    name: str
    age: int
    id: int

path_actions_log = Path(__file__).parent.parent / "CSVs" / "Class48_log.txt"
path_actions_log.parent.mkdir(parents=True, exist_ok=True)
path_actions_log.touch(exist_ok=True)

employee_list: list[Employee] = []

def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        action = func.__name__
        if func == True:
            with open(path_actions_log, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([f"Action completada: {action}, Name: {args[1]['name']}, Age: {args[1]['name']}, ID: {args[1]['id']}"])
            return result
        else:
            with open(path_actions_log, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([f"Action fallida: {action}, Name: {args[1]['name']}, Age: {args[1]['name']}, ID: {args[1]['id']}"])
            return result
    return wrapper


@log_action
def add_employee(employee_list: list[Employee], employee: Employee) -> None:
    if not isinstance(employee['name'], str) or not isinstance(employee['age'], int) or not isinstance(employee['id'], int):
        raise TypeError("Employee fields must be of correct types: name (str), age (int), position (str)")
    elif employee['id'] in [emp['id'] for emp in employee_list]:
        raise ValueError(f"Employee with id {employee['id']} already exists.")
    else:
        employee_list.append(employee)
        return True

@log_action
def delete_employee(employee_list: list[Employee], employee_id: int) -> None:
    for i, emp in enumerate(employee_list):
        if emp['id'] == employee_id:
            del employee_list[i]
            return True
    raise ValueError(f"Employee with id {employee_id} not found.")

def employee_manager():
    while True:
        action = input("Choose an action: add, delete, exit: ").strip().lower()
        if action == "add":
            try:
                name = input("Enter employee name: ")
                age = int(input("Enter employee age: "))
                emp_id = int(input("Enter employee id: "))
                new_employee: Employee = {"name": name, "age": age, "id": emp_id}
                add_employee(employee_list, new_employee)
                print(f"Employee {name} added successfully.")
            except (TypeError, ValueError) as e:
                print(e)
        elif action == "delete":
            try:
                emp_id = int(input("Enter employee id to delete: "))
                delete_employee(employee_list, emp_id)
                print(f"Employee with id {emp_id} deleted successfully.")
            except ValueError as e:
                print(e)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please choose add, delete, or exit.")

if __name__ == "__main__":
    employee_manager()