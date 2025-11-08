from pathlib import Path


print('///////////////////////////////')
current_dir = Path.cwd()
script_dir = Path(__file__).parent
file_path = current_dir / 'Codedex' / 'Diary.csv'
script_path = script_dir / 'Diary.csv'

#file_path.write_text("nombre,edad\nEsteban,25")
#print("Archivo creado en:", file_path)


file = open(script_path, 'x', encoding='utf-8')
file.write('''Deberia poder hacerlo, yes''')