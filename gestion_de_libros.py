"""
Ejercicio de Gestión de Libros:
Implementa un programa que permita gestionar una lista de libros. Cada libro debe tener un título, 
un autor y un año de publicación. Proporciona opciones para agregar nuevos libros, mostrar la lista de libros 
y buscar libros por autor.
"""

# Definición de la clase Book que representa un libro con título, autor y año de publicación
class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __repr__(self):
        return f"{self.title} (Author: {self.author}, Year: {self.year})"

# Función para mostrar la lista de libros
def show_books(books):
    if not books:
        print("No book has been uploaded yet")
    else:
        print("Available books")
        for i, book in enumerate(books):
            print(f"{i + 1}. {book}")

# Función para agregar un nuevo libro
def add_book():
    title = str(input("Input the book's title: "))
    author = str(input("Input the author's name: "))
    year = int(input("Input the year of publication: "))
    
    return Book(title, author, year)

# Lista que almacenará los libros
books = []

# Bucle principal del programa
while True:
    print("")
    print("1. Add book")
    print("2. Show books")
    print("3. Search book by author")
    print("4. Exit")
    option = input("Choose an option: ")
    print("")

    # Bloques condicionales para manejar las opciones del usuario
    if option == "1":
        # Agregar un nuevo libro
        new_book = add_book()
        books.append(new_book)
        
    elif option == "2":
        # Mostrar la lista de libros
        if len(books) < 1:
            print("No books available to show")
        else:
            show_books(books)
            
    elif option == "3":
        # Buscar libros por autor
        author_sought = input("Input the author's name: ")
        
        # Utilizamos un bucle for para buscar libros por autor
        found_books = []
        for book in books:
            if book.author == author_sought:
                found_books.append(book)

        # Verificamos si se encontraron libros y los mostramos
        if found_books:
            print("Books by the specified author:")
            for found_book in found_books:
                print(found_book)
        else:
            print(f"No books found for the author: {author_sought}")
    
    elif option == "4":
        # Salir del programa
        print("End of the program")
        break
    else:
        print("Invalid option")
        
        
"""
| Paso | Entradas del Usuario                                                | Estado de la Lista de Libros                                                | Salida Esperada                                 |
|------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------|
| 1    | Opción: 1                                                           | Lista de libros vacía                                                       | -                                               |
| 2    | Título: The Hunger Games<br>Autor: Suzanne Collins<br>Año: 2008     | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008)]                 | -                                               |
| 3    | Título: To Kill a Mockingbird<br>Autor: Harper Lee<br>Año: 2008     | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | Mensaje de opción inválida                      |
| 5    | Título: Pride and Prejudice<br>Autor: Jane Austen<br>Año: 1813      | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | -                                               |
| 6    | Opción: 3<br>Autor buscado: 2                                       | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | Mensaje de no encontrar libros para el autor: 2 |
| 7    | Opción: 2                                                           | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | Se muestra la lista de libros                   |
| 8    | Opción: A Game of Thrones                                           | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | Mensaje de opción inválida                      |
| 9    | Título: A Game of Thrones<br>Autor: George R.R. Martin<br>Año: 1996 | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | -                                               |
| 10   | Título: A Clash of Kings<br>Autor: George R.R. Martin<br>Año: 1998  | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | -                                               |
| 11   | Opción: 2                                                           | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),...              | Se muestra la lista de libros                   |
| 12   | Opción: 3<br>Autor buscado: George R.R. Martin                      | [1. A Game of Thrones (Author: George R.R. Martin, Year: 1996),2. A Clash...| Se muestran los libros de George R.R. Martin    |
| 13   | Opción: 4                                                           | [1. The Hunger Games (Author: Suzanne Collins, Year: 2008),<br>2. To Kill...| Mensaje de despedida                            |
"""