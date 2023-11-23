"""
Crea un programa que gestione un registro de estudiantes. Cada estudiante debe tener un nombre, una edad y una lista de asignaturas en las que está inscrito. 
Proporciona opciones para agregar nuevos estudiantes, mostrar la lista de estudiantes y buscar estudiantes por asignatura.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = []
    
    def register_subject(self, subject):
        self.subjects.append(subject)
        print(f"{self.name} se ha inscrito en la asignatura de: {subject}")
    
    def __repr__(self):
        return f"{self.name}, {self.age}. - Asignaturas: {self.subjects}"

#-------------------------------------------------------------------------------------------------- #

def add_student():
        name = input("Ingrese el nombre del estudiante: ")
        age = int(input("Ingrese la edad del estudiante: "))
        
        student = Student(name, age)

        while True:
            subject = input("Ingrese una asignatura (o escriba 'fin' para terminar): ")
            if subject.lower() == 'fin':
                break
            else:
                student.register_subject(subject)
                
        return student

def show_students(students):
    if not students:
        print("No hay estudiantes para mostrar")
    else:
        print("- Estudiantes registrados -")
        for i, student in enumerate(students):
            print(f"{i + 1}. {student}")

#-------------------------------------------------------------------------------------------------- #

students = []

while True:
    print("")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")
    option = input("Selecciona una opcion: ")
    print("")
    
    if option == "1":
        new_student = add_student()
        students.append(new_student)
    
    elif option == "2":
        show_students(students)
    
    elif option == "3":
        students_found = []
        show_subject = input("Ingrese la asignatura que desea buscar: ")

        for student in students:
            if show_subject in student.subjects:  # Corregir la comparación aquí
                students_found.append(student)

        if students_found:
            print(f"Estudiantes cursando {show_subject}:")
            for student_found in students_found:
                print(student_found)
        else:
            print("No hay alumnos cursando esa materia.")  
            
    elif option == "4":
        print("Fin del programa")
        break
    else:
        print("Opción invalida. Seleccione nuevamente.")