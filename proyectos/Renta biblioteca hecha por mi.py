class Book:
    def __init__(self, name: str, author: str, price: float):
        self.name = name
        self.author = author
        self.price = price
        self.available = True
    
    def get_price(self):
        return self.price
    def get_price_promotion(self):
        return self.price * 0.90
    
    def borrow_book(self,):
        while True:
            promocion_options = ["si", "yes", "no",]
            promocion = input("Esta el libro en una promocion: ").strip().lower()
            if promocion == "no":
                if self.available:
                    self.available = False
                    print(f"El libro \"{self.name}\" del autor {self.author} ha sido prestado por {self.get_price()}")
                    return
            elif promocion == "si" or promocion == "yes":
                if self.available:
                    self.available = False
                    print(f"El libro \"{self.name}\" del autor {self.author} ha sido prestado en una promocion por {self.get_price_promotion()}")
                    return
            elif promocion not in promocion_options:
                print("\nEsa no es una opcion valida\nOpciones validas: \"Si\", \"Yes\", \"No\"")
        
    def return_book(self,):
        self.available = True
        print(f"El libro {self.name} ha sido retornado correctamente")

class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow_book()
            self.borrowed_books.append(book)
        else:
            print(f"El libro \"{book.name}\" no se encuentra disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.name} no se encuentra en tu coleccion por tanto no puedes retornarlo")
    
    def show_borrowed_books(self):
        print("Tus libros prestados son: ")
        for b in self.borrowed_books:
            print(f"{b.name} por {b.author}")

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []
    
    def add_book(self, book):
        if book in self.books:
            print(f"El libro \"{book.name}\" por {book.author} ya se encuentra agregado a un precio de: {book.price}")
        else:
            self.books.append(book)
            print(f"El libro \"{book.name}\" por {book.author} ha sido agregado a un precio de: {book.price}")
    
    def add_user(self, user):
        if user in self.users:
            print (f"El usuario {user.name} con id {user.id} ya esta en nuestro sistema")
        else:
            self.users.append(user)
            print(f"El usuario {user.name} con id {user.id} ha sido agregado correctamente")

    def show_books(self):
        availability = "disponible"
        print("La lista de libros en nuestra biblioteca es la siguiente: ")
        for b in self.books:
            availability = "Disponible" if b.available else "No disponible"
            print(f"{b.name} por {b.author} aun precio de {b.price}. {availability}")

    def show_available_books(self):
        print("Los libros disponibles son:")
        for b in self.books:
            if b.available:
                print(f"{b.name} por {b.author} aun precio de {b.price}")
    def show_unavailable_books(self):
        print("Los libros no disponibles son:")
        for b in self.books:
            if b.available == False:
                print(f"{b.name} por {b.author}")





        pass

book1 = Book("El archivo de las tormentas", "Brandon sanderson", 1200)
book2 = Book("Nacidos de la bruma", "Brandon sanderson", 1300)
user1 = User("Esteban", 687218)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.show_books()
user1.borrow_book(book1)
library.show_books()
library.show_available_books()
library.show_unavailable_books()
