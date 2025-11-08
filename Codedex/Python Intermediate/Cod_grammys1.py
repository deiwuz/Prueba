from typing import List, Tuple
from functools import reduce
from operator import itemgetter

playlist: List[Tuple[str, float]] = [
    ('What Was I Made For?', 3.42),
    ('Just Like That', 5.05),
    ('Song 3', 6.55),
    ('Leave The Door Open', 4.02),
    ("I Can't Breath", 4.47),
    ('Bad Guy', 3.14),
]

def longer_than_five_minutes(song: List[Tuple[str, float]]):
    name, minutes = song
    return minutes > 5

Songs_longer_five = filter(longer_than_five_minutes, playlist)
print(list(Songs_longer_five))

def minutes_to_seconds(song: List[Tuple[str, float]]):
    title, minutes = song
    return (title, minutes * 60)

playlist_in_seconds: List[Tuple[str, float]] = list(map(minutes_to_seconds, playlist))
print(f"Playlist (seconds): {playlist_in_seconds}")

# individual

Individual_seconds : List[tuple[str, float]] = list(map(itemgetter(1), playlist_in_seconds))
print(f"Playlist with only duration : {Individual_seconds}")

def add_durations(x: int, y: int) -> float:
    return x + y

total_seconds : float = reduce(add_durations, Individual_seconds, 0.0)
total_minutes : float = reduce(add_durations, map(itemgetter(1), playlist), 0.0)

print(f"the total playtime its: {total_minutes} minutes or {total_seconds:.02f} seconds")
