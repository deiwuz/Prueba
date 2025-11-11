#########
# Clase 45 Ejercicio Autonomo
##########
"""
Sistema de Gestión de Biblioteca con Decoradores

Este módulo demuestra el uso de decoradores y decorator factories en Python:
- Decorator factory: check_access() - Valida permisos de acceso con parámetros
- Decoradores simples: check_book_availability, log_action
- Transformación de parámetros en decoradores
- Stack de múltiples decoradores
- Uso de @wraps para preservar metadata de funciones

El sistema permite:
- Listar libros disponibles
- Leer libros con validación de permisos y disponibilidad
- Registro automático de acciones y errores en archivo de log
"""
from typing import Any, TypedDict
from datetime import datetime
from functools import wraps
from pathlib import Path
import csv

###############################
# Definicion de tipos

class Book(TypedDict):
    title: str
    author: str
    year: int
class Reader(TypedDict):
    name: str
    member_id: int
    full_access: bool

readers = {
    101: {'name': 'Carlos', 'member_id': 101, 'full_access': True},
    102: {'name': 'Ana', 'member_id': 102, 'full_access': False},
    103: {'name': 'Luis', 'member_id': 103, 'full_access': True},
    104: {'name': 'Marta', 'member_id': 104, 'full_access': False},
    105: {'name': 'Sofia', 'member_id': 105, 'full_access': True},
}


###############################
# Rutas de los archivos
###############################

library_path = Path(__file__).parent.parent / 'CSVs' / 'library' / 'library.csv'
library_path.parent.mkdir(parents=True, exist_ok=True)  # Crear directorio si no existe
library_log_path = library_path.parent / 'library_log.txt'
library_log_path.touch(exist_ok=True)  # Crear archivo si no existe

##############################
# Funcion para cargar la lista de libros
##############################

def load_library() -> list[dict[str, str | int]]:
    """
    Carga la lista de libros desde el archivo CSV de la biblioteca.

    Returns:
        list[dict[str, str | int]]: Lista de diccionarios con información de cada libro.
                                    Cada diccionario contiene: title, author, year
    """
    with open(library_path, 'r', newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

##############################
# Decoradores
##############################

def check_access(access_required: bool):
    """
    Decorator factory que verifica si un lector tiene el nivel de acceso requerido.

    Este es un ejemplo de decorator factory porque recibe un parámetro (access_required)
    y retorna un decorador que puede ser aplicado a funciones.

    Args:
        access_required (bool): Nivel de acceso requerido (True = acceso completo, False = acceso limitado)

    Returns:
        function: Decorador que valida el acceso antes de ejecutar la función
    """
    def decorator(func):
        @wraps(func)
        def wrapper(reader: Reader, *args, **kwargs):
            # Verificar si el lector tiene el nivel de acceso requerido
            if reader.get('full_access') == access_required:
                print(f"Acceso concedido al lector {reader['name']}")
                return func(reader, *args, **kwargs)
            else:
                # Denegar acceso y registrar el intento
                print(f"El lector {reader['name']} no tiene permisos para ejecutar esta accion. Se requiere acceso completo.")
                with open(library_log_path, 'a', newline='', encoding='utf-8') as log_file:
                    log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Lector: {reader['name']} - Accion: {func.__name__} - Acceso denegado\n")
                return
        return wrapper
    return decorator
def check_book_availability(func):
    """
    Decorador que verifica si un libro está disponible en la biblioteca.

    Este decorador transforma los parámetros: recibe (reader, book_title) desde el caller
    y pasa (reader, book_object) a la función decorada. Esto evita búsquedas duplicadas
    y es un patrón avanzado de decoradores.

    Args:
        func: Función a decorar que espera recibir (reader, book_object)

    Returns:
        function: Función wrapper que valida disponibilidad y transforma parámetros
    """
    @wraps(func)
    def wrapper(reader: Reader, book_title: str, *args, **kwargs):
        # Cargar la biblioteca y buscar el libro
        library = load_library()
        for book in library:
            if book['title'].lower() == book_title.lower():
                # Pasar el objeto book completo en lugar de solo el título
                # Esto evita que la función decorada tenga que buscar nuevamente
                return func(reader, book, *args, **kwargs)

        # Si el libro no se encuentra, registrar y retornar sin ejecutar la función
        print(f"El libro '{book_title}' no esta disponible en la biblioteca.")
        with open(library_log_path, 'a', newline='', encoding='utf-8') as log_file:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Lector: {reader['name']} - Accion: {func.__name__} - Libro: {book_title} - No disponible\n")
        return
    return wrapper
def log_action(func):
    """
    Decorador que registra todas las acciones exitosas en un archivo de log.

    Este decorador se ejecuta DESPUÉS de las validaciones (por su posición en el stack),
    por lo que solo registra acciones que pasaron todos los controles previos.

    Args:
        func: Función a decorar

    Returns:
        function: Función wrapper que registra la acción antes de ejecutarla
    """
    @wraps(func)
    def wrapper(reader: Reader, book: dict[str, str | int], *args, **kwargs):
        print(f"Iniciando registro de accion para {reader['name']}")
        # Registrar la acción en el archivo de log con timestamp
        with open(library_log_path, 'a', newline='', encoding='utf-8') as log_file:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Lector: {reader['name']} - Accion: {func.__name__} - Libro: {book['title']}\n")
        return func(reader, book, *args, **kwargs)
    return wrapper

@check_access(True)
@check_book_availability
@log_action
def read_book(reader: Reader, book: dict[str, str | int]) -> None:
    """
    Permite a un lector leer un libro de la biblioteca.

    Esta función está decorada con tres decoradores que se ejecutan en orden:
    1. check_access(True) - Verifica que el lector tenga acceso completo
    2. check_book_availability - Valida que el libro exista y transforma book_title a book_object
    3. log_action - Registra la acción exitosa en el log

    Args:
        reader (Reader): Información del lector (name, member_id, full_access)
        book (dict[str, str | int]): Objeto libro con title, author, year
                                     (transformado por el decorador check_book_availability)

    Note:
        El parámetro que recibe esta función (book) es diferente al que se pasa al llamarla (book_title).
        Los decoradores realizan la transformación automáticamente.
    """
    # No es necesario buscar nuevamente - el decorador ya validó y proporcionó el libro
    print(f"El lector {reader['name']} esta leyendo '{book['title']}' de {book['author']} ({book['year']})")

def show_books_in_library() -> None:
    """
    Muestra todos los libros disponibles en la biblioteca.

    Carga el catálogo completo desde el archivo CSV y lo imprime en formato legible.
    """
    library = load_library()
    print("Los libros disponibles en la biblioteca son:")
    for book in library:
        print(f"- {book['title']} por {book['author']} ({book['year']})")

def library_menu() -> None:
    """
    Menú interactivo principal del sistema de biblioteca.

    Presenta un menú con las siguientes opciones:
    1. Mostrar libros disponibles - Lista todos los libros del catálogo
    2. Leer un libro - Permite a un lector leer un libro (con validaciones de acceso)
    3. Salir - Termina el programa

    El menú se ejecuta en un bucle hasta que el usuario seleccione salir.
    """
    while True:
        print("1. Mostrar libros disponibles")
        print("2. Leer un libro")
        print("3. Salir")
        option = input("Seleccione una opcion: ")

        if option == "1":
            show_books_in_library()
        elif option == "2":
            # Solicitar ID del lector y título del libro
            input_id = int(input("Ingrese el ID del lector: "))
            input_book_title = input("Ingrese el titulo del libro: ")

            # Validar que el lector existe en la base de datos
            if input_id in readers.keys():
                read_book(readers[input_id], input_book_title)
            else:
                print(f"Lector con id {input_id} no encontrado en la base de datos.")
                continue
        elif option == "3":
            print("Saliendo del menu de la biblioteca")
            break
        else:
            print("Opcion no valida")

def main():
    """
    Punto de entrada principal del programa.

    Inicia el menú interactivo de la biblioteca.
    """
    library_menu()

if __name__ == "__main__":
    main()