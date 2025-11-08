from pathlib import Path
import csv

file_dir = Path(__file__).parent / 'message.txt'

with open(file_dir, 'r+', newline="", encoding='utf-8') as file:
    file.write('Hey there! This is a secret message.')

    file.seek(0)

    file.write('This message has been unsent.')

    file.truncate()