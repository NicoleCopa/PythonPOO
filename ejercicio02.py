class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age) #This is inherited from the parent class
        self.grade = grade
        
    def show_grade(self):
        print(f"Grade: {self.grade}")

student = Student("Juan", "24", "10mo")
student.show_data()
student.show_grade()