# Write code below 💖
from typing import List, Tuple

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

###################
#####1. filter#####
###################

def filter_min(list: List) -> List:
    '''
    Retorna las canciones con duracion superior a 5 minutos
    '''
    return list[1] > 5

longer_than_five_minutes = filter(filter_min, playlist)
print(list(longer_than_five_minutes))

####################
#######2. map#######
####################

songs_in_seconds = []

def minutes_to_seconds(list: List) -> List:
    '''
    Retorna cada valor de la lista multiplicado por 60
    '''
    return list[1] * 60

minutes_sec = map(minutes_to_seconds, playlist) # Toma cada valor de minutes_to_seconds y los agrega a la lista songs_in_seconds
for s in list(minutes_sec):
    songs_in_seconds.append(s) # 
print (songs_in_seconds)

####################
######3. reduce#####
####################

from functools import reduce

time = []


for s in playlist:
    time.append(s[1])

def add_durations(x: float, y: float) -> float:
    '''
    Retorna la suma de cada uno de los valores de una lista
    '''
    return x + y

added_durations = reduce(add_durations, time) # Calcula la suma en minutos de todas las canciones
added_second_durations = reduce(add_durations, songs_in_seconds) # Calcula la suma en segundos de todas las canciones

print(f"the total playtime its: {added_durations}m or {added_second_durations:.02f} seconds")
