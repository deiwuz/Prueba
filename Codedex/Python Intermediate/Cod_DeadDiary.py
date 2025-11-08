from pathlib import Path
import csv
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

terminal_directory = Path.cwd()
file_path = Path(__file__).parent / 'Diary.csv'

# with open(file_path, 'a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Hola"])


fieldnames = 'fecha', 'nota'

with open(file_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    if f.tell() == 0:
        writer.writeheader()
    
    writer.writerow({'fecha': today, 'nota': "Aprendiendo"})
    
