from pathlib import Path
import csv

IN_PATH = Path(__file__).parent / 'Bestsellers - Sheet1.csv'
OUT_PATH = Path(__file__).parent / 'Bestseller.csv'

FIELDNAMES = 'Author', 'sales in millions', 'Book', 'First published', 'Genre', 'Original language'

def parse_value(value: str) -> float:
    '''
    Toma un valor de tipo str y lo convierte a flotante
    '''
    if value is None:
        return 0.0
    txt = value.strip().replace(",", "")
    if txt == "" or txt.lower() == "n/a":
        return 0.0
    try:
        return float(txt)
    except ValueError: # Si la conversion a flotante fallo retorna 0.0
        return 0.0

def get_best_seller(in_path: Path) -> dict[str, str]:
    '''
    Lee un archivo csv y retorna el libro con mayor numero de ventas.
    '''
    with open(in_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if r.get('Book')] # Agrega cada una de las filas a lista Rows si la fila contine la llave 'Book' y no esta vacia ""
        if not rows:
            raise ValueError("Tu archivo no contiene filas validas") # Si ninguna fila contiene la llave 'Book' notifica al usuario
        return max(rows, key=lambda r: parse_value(r.get('sales in millions', '0'))) # Retorna el libro que tenga mas ventas, si el valor de una llave 'sales in millions' no existe lo cambia 0 para que no de error

def write_best_seller(in_path: Path, out_path: Path) -> None:
    '''
    Escribe en un archivo csv el libro con mayor numero de ventas
    obtenido de get_best_seller
    '''
    with open(out_path, 'w', newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction='ignore')
        if f.tell() == 0:
            writer.writeheader() # Si el archivo no tiene nada escribe los headers
        writer.writerow(get_best_seller(in_path))

write_best_seller(IN_PATH, OUT_PATH)
