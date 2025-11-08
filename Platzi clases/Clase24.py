class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.avaiblable = False
            print(f"El libro {self.title} ha sido prestado")
        
        else:
            print(f"El libro {self.title} no esta disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} se ha retornado")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no esta disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no esta en la lista de prestado")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")
    
    def reg_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_books(self):
        print("Los libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

#Crear libros
book1 = Book("El archivo de las tormentas", "Brandon Sanderson")
book2 = Book("Brazales de duelo", "Brandon")
book3 = Book("Nacidos de la bruma", "Sanderson")

#Crear Usuario
user1 = User("Esteban", "001")

#Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.reg_user(user1)

#Mostar libros
library.show_books()

#Realizar prestamo
user1.borrow_book(book1)

library.show_available_books()