from pathlib import Path
import csv

file_dir = Path(__file__).parent / 'Playlist.csv'

playlist = [
    {"artist": "Guitarricadelafuente", "song": "Mil y Una Noches"},
    {"artist": "Corey Taylor", "song": "Snuff (Acoustic)"},
    {"artist": "Bastille", "song": "Pompeii"},
    {"artist": "Buccini", "song": "Sick of You (Sped Up)"},
    {"artist": "Rocío Dúrcal", "song": "La Gata Bajo La Lluvia"},
    {"artist": "Lana Del Rey", "song": "Summertime Sadness"},
    {"artist": "David Bowie", "song": "Starman"},
    {"artist": "Steve Lacy", "song": "Static"},
    {"artist": "Rosa Walton & Hallie Coggins", "song": "I Really Want to Stay at Your House"},
    {"artist": "Zach Bryan", "song": "Something In The Orange"},
    {"artist": "The Game ft. 50 Cent", "song": "Hate It Or Love It"},
    {"artist": "Sam Smith ft. Kim Petras", "song": "Unholy"},
    {"artist": "Café Tacvba", "song": "Aviéntame (En Vivo)"},
    {"artist": "Café Tacvba", "song": "Cuentame"},
    {"artist": "Gorillaz", "song": "Feel Good Inc."},
    {"artist": "C. Tangana", "song": "Demasiadas Mujeres"},
    {"artist": "Gorillaz", "song": "Clint Eastwood"},
    {"artist": "C. Tangana", "song": "Tú Me Dejaste De Querer"},
    {"artist": "Kanye West", "song": "Bound 2"},
    {"artist": "Gerry Rafferty", "song": "Right Down the Line"},
    {"artist": "Lana Del Rey", "song": "Dealer"},
    {"artist": "Rodrigo Amarante", "song": "Tuyo (Narcos Theme)"},
    {"artist": "Lana Del Rey", "song": "Watercolor Eyes"},
    {"artist": "Kevin Kaarl", "song": "Vete"},
    {"artist": "Never Get Used To People", "song": "Life Letters (Long Version)"},
    {"artist": "Calibre 50", "song": "Si Te Pudiera Mentir"},
    {"artist": "Edison Lighthouse", "song": "Love Grows (Where My Rosemary Goes)"},
    {"artist": "Calle 13", "song": "La Vuelta al Mundo"},
    {"artist": "Anthrés", "song": "Si la noche es infinita como tú"},
    {"artist": "Ed Maverick", "song": "El Fuego En El Cielo"},
    {"artist": "Anthrés", "song": "No te rindas en mí"},
    {"artist": "Fallen Roses", "song": "Idk."},
    {"artist": "Willow Smith", "song": "Wait a Minute!"},
    {"artist": "Shiloh Dynasty & CuBox", "song": "Losing Interest"},
    {"artist": "Mac Miller", "song": "Love Lost"},
    {"artist": "Mild High Club", "song": "Homage"},
    {"artist": "Kevin Kaarl", "song": "Abrazado a Ti"},
    {"artist": "Trueno", "song": "DANCE CRIP"},
    {"artist": "Coldplay", "song": "Fix You"},
    {"artist": "Beabadoobee", "song": "The Moon Song"},
    {"artist": "ミラクルミュージカル", "song": "Dream Sweet in Sea Major"},
    {"artist": "Adele", "song": "Rolling in the Deep"},
    {"artist": "Sufjan Stevens", "song": "Mystery of Love"},
    {"artist": "Sufjan Stevens", "song": "Visions of Gideon"},
    {"artist": "Sufjan Stevens", "song": "Should Have Known Better"},
    {"artist": "Sufjan Stevens", "song": "Futile Devices"},
    {"artist": "Patrick Watson", "song": "Je te laisserai des mots"},
    {"artist": "AURORA", "song": "The Seed"},
    {"artist": "Gorillaz", "song": "Humility"},
    {"artist": "Frédéric Chopin", "song": "Nocturne op.9 No.2"},
    {"artist": "AURORA", "song": "Cure For Me"},
    {"artist": "Riot Games Music", "song": "Dynasties & Dystopia"},
    {"artist": "Riot Games Music", "song": "Dirty Little Animals"},
    {"artist": "Riot Games Music", "song": "Playground"},
    {"artist": "Hozier", "song": "Work Song"},
    {"artist": "Hozier", "song": "Cherry Wine"},
    {"artist": "XXXTENTACION", "song": "Revenge"},
    {"artist": "XXXTENTACION", "song": "Moonlight"},
    {"artist": "XXXTENTACION", "song": "Look At Me!"},
    {"artist": "XXXTENTACION", "song": "NUMB"},
    {"artist": "XXXTENTACION", "song": "Angel"},
    {"artist": "XXXTENTACION", "song": "Jocelyn Flores"},
    {"artist": "XXXTENTACION", "song": "SAD!"},
    {"artist": "XXXTENTACION", "song": "Everybody Dies In Their Nightmares"},
    {"artist": "XXXTENTACION ft. Trippie Redd", "song": "Fuck Love"},
    {"artist": "Pomplamoose", "song": "Bust Your KneeCaps"},
    {"artist": "The Dø", "song": "Take Away Show"},
    {"artist": "Ramsey", "song": "Goodbye"},
    {"artist": "Sting", "song": "What Could Have Been"},
    {"artist": "Kevin Kaarl", "song": "Tú Si Eres Real"},
    {"artist": "The Neighbourhood", "song": "Daddy Issues"},
    {"artist": "carolesdaughter", "song": "Violent"},
    {"artist": "fousheé", "song": "Deep End"},
    {"artist": "AURORA", "song": "Runaway"},
    {"artist": "AURORA", "song": "Queendom"},
    {"artist": "AURORA", "song": "Running With The Wolves"},
    {"artist": "Sub Urban ft. AURORA", "song": "PARAMOUR"},
    {"artist": "AURORA", "song": "Exist For Love"},
    {"artist": "AURORA", "song": "Conqueror"},
    {"artist": "AURORA", "song": "Giving In To The Love"},
    {"artist": "Ed Maverick", "song": "Fuentes De Ortiz"},
    {"artist": "AURORA", "song": "Animal"},
    {"artist": "AURORA", "song": "Murder Song (5, 4, 3, 2, 1)"},
    {"artist": "Sub Urban", "song": "Cradles"},
    {"artist": "Sub Urban", "song": "BANDIT"},
    {"artist": "Sub Urban ft. REI AMI", "song": "Freak"},
    {"artist": "Sub Urban ft. BENEE", "song": "UH OH!"},
    {"artist": "Sub Urban", "song": "Cirque"},
    {"artist": "Childish Gambino", "song": "This Is America"},
    {"artist": "The Weeknd ft. Daft Punk", "song": "Starboy"},
    {"artist": "The Weeknd ft. Lana Del Rey", "song": "Stargirl Interlude"},
    {"artist": "Harry Styles", "song": "As It Was"},
    {"artist": "girl in red", "song": "rue"},
    {"artist": "Bratty", "song": "jules"},
    {"artist": "Imagine Dragons ft. J.I.D", "song": "Enemy"}
]

'''
Escribir la lista como diccionario en un archivo csv
'''
fieldnames = ["artist", "song"]

with open(file_dir, 'w', newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    if file.tell() == 0:
        writer.writeheader()
    
    writer.writerows(playlist)

'''
Leer la lista del archivo csv
'''

with open(file_dir, 'r', newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['artist']} - {row['song']}")