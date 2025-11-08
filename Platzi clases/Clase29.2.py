class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"{self.name}, {self.age} años")
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def greet(self):
        super().greet()
        print(f"Person(name={self.name}, age={self.age})")
    

person1 = Person("Esteban", 21)
#person1.greet()

student1 = Student("Esteban", 21, 687218)

student1.greet()
