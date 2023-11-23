"""
Ejercicio de Gestión de Libros:
Implementa un programa que permita gestionar una lista de libros. Cada libro debe tener un título, 
un autor y un año de publicación. Proporciona opciones para agregar nuevos libros, mostrar la lista de libros 
y buscar libros por autor.
"""

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __repr__(self):
        return f"{self.title} (Author: {self.author}, Year: {self.year})"