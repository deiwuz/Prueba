# Write code below 💖

import random

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
    return name.capitalize()

capitalized_suffix = list(map(capitalize_suffix, suffixes))

random_names = [name + create_fantasy_name for name in range]

print(random_names)