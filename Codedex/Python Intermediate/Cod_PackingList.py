from pathlib import Path
import csv

PATH = Path(__file__).parent / 'packing_list.csv'
FIELDNAMES = ['Item' 'Blender' 'Posters' 'Shoes']


data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

def packing_list(path: Path) -> dict:
    try:
        with open(path, 'r', newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [r for r in reader]
            print(rows)
    except FileNotFoundError:
            print("Packing list file not found. Creating a new one.")
            with open(path, 'w', newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)

packing_list(PATH)