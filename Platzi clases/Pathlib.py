import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(Base_dir, 'subdir')
#Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: Base_dir / 'subdir'.
#base_dir = Path(__file__).resolve().parent.parent


#print directory that we are working in
#print(Path.cwd())

#iterate trough directorys
#for p in Path().iterdir():
 #   print(p)

#create path object
my_dir = Path('proyectos')
my_file = Path('correcion.py')

#get the suffix
#print(my_dir.suffix)
#print(my_file.suffix)

#get the name
#print(my_dir.name)
#print(my_file.name)

#get the stem
print(my_file.stem)

#Work on a file in a directory
new_file = my_dir / "new_file.txt"

#Check if it exist
print(new_file.exists())