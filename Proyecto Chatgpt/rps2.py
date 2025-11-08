import random
import csv
from pathlib import Path


import os, sys, platform
print("cwd:", os.getcwd())
print("python:", sys.executable)
print("platform:", platform.system(), platform.release())

def rock_paper_scissors():

    options: list[str] = ['rock', 'paper', 'scissors']
    winning_options: dict[str, str] = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    def evaluate_round(player: str, cpu: str):
        if player == cpu:
            return "It's a tie!"
        elif winning_options[player] == cpu:
            return "You win!"
        else:
            return "You lose!"
        
    def save_result(player: str, cpu: str, result: str):
        file_path = Path('C:/Users/Esteban/Documents/Aprendizaje/Proyecto Chatgpt/game_history.csv') 
        with open(file_path, mode='a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([player, cpu, result])

    def game():
        print ("=== Rock, Paper, Scissors (with CSV history) ===")

        while True:
            player = input('Choose rock, paper, or scissors (choose "exit" to quit): ').lower()

            if player == 'exit':
                print('Thanks for playing!')
                break

            if player not in options:
                print('Invalid choice, please try again')
                continue

            cpu = random.choice(options)
            result = evaluate_round(player, cpu)

            print(result)
            
            save_result(player, cpu, result)
    
    game()

rock_paper_scissors()



