class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def greet(self):
        print(f"hello mi name is {self.name} and im {self.age} years old")
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        super().greet()
        print(f"Hello im student: {self.student_id}")

student1 = Student("Esteban", 20, 687218)

student1.greet()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def greet(self):
        print(f"hello mi name is {self.name} and im {self.age} years old")
    
class Student(Person):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
    
    def greet(self):
        print(f"Hello im student: {self.student_id}")

student1 = Student("Esteban", 20, 687218)

student1.greet()