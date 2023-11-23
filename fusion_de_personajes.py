"""
Ejercicio de Fusión de Personajes:
Implementa una aplicación simple para gestionar personajes utilizando la clase Personaje. Cada personaje tiene un nombre, 
una fuerza y una velocidad. Además, puedes fusionar dos personajes para crear uno nuevo con características combinadas.
"""

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    #mostrar personaje
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro):
        nuevo_nombre = self.nombre + "-" + otro.nombre
        nueva_fuerza = round(((self.fuerza + otro.fuerza) /2) ** 1.5)
        nueva_velocidad = round(((self.velocidad + otro.velocidad) /2) ** 1.3)
        
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

# ------------------------------------------------------------------------------------------ #

def mostrar_personajes(personajes):
    if not personajes:
        print("Aún no ha creado ningun personaje.")
    else:
        print("Personajes disponibles:")
        for i, personaje in enumerate(personajes):
            print(f"{i + 1}. {personaje}")
        

def crear_personaje():
    nombre = str(input("Ingrese el nombre del personaje: "))
    fuerza = float(input("Ingrese la fuerza del personaje: "))
    velocidad = float(input("Ingrese la velocidad del personaje: "))
    
    return Personaje(nombre, fuerza, velocidad)

personajes = []

while True:
    print("")
    print("1. Crear personaje")
    print("2. Fusionar personaje")
    print("3. Mostrar personajes")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    print("")
    
    if opcion == "1":
        personaje_nuevo = crear_personaje()
        personajes.append(personaje_nuevo)
    
    elif opcion == "2":
        if len(personajes) < 2:
            print("Debe tener al menos dos personajes para fusionar.")
        else:
            mostrar_personajes(personajes)
            num_pj1 = int(input("Ingrese el número del personaje: "))
            num_pj2 = int(input("Ingrese el número del segundo personaje: "))
            
            if 1 <= num_pj1 <= len(personajes) and 1 <= num_pj2 <= len(personajes) and num_pj1 != num_pj2:
                personaje1 = personajes[num_pj1 - 1]
                personaje2 = personajes[num_pj2 - 1]
                
                personaje_fusionado = personaje1 + personaje2
                personajes.append(personaje_fusionado)
                
                print(f"Funsión exitosa - El nuevo personaje es: {personaje_fusionado}")
            
            else:
                print("Seleccion inválida. Elija otra vez")
        
    elif opcion == "3":
        mostrar_personajes(personajes)
    
    elif opcion == "4":
        print("A D I O S")
        break
    
    else:
        print("Opcion invalida. Seleccione una valida")
