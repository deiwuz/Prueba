def add_employee_ids(id1: int, id2: int,) -> int:
    return id1 + id2

print(add_employee_ids(10, 20))

class Employee:
    name: str
    age: int
    id: int
    salary: float
    
    def __init__(self, name: str, age:int, id: int, salary: float):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
        
    def greet(self) -> str:
        return f"Hola mi nombre es {self.name} y tengo {self.age} anos"
        pass

emp1 = Employee("Esteban", 21, 687218, 2600.00)

print(emp1.greet())