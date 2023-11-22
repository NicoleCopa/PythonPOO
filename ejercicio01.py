class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando")
    
nombre = str(input("Ingrese el nombre del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))
grado = str(input("Ingrese el grado del estudiante: "))

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE
      Nombre: {estudiante.nombre}
      Edad: {estudiante.edad}
      Grado: {estudiante.grado}
      """)

estudiante.estudiar()

"""
Ingrese el nombre del estudiante: Juan
Ingrese la edad del estudiante: 25
Ingrese el grado del estudiante: Primero

      DATOS DEL ESTUDIANTE
      Nombre: Juan
      Edad: 25
      Grado: Primero

Juan está estudiando
"""