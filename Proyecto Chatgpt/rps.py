import random
import csv

options: list[str] = ['rock', 'paper', 'scissors']
winning_options: dict[str, str] = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

def game():
    while True:
        player = input('Choose rock, paper, or scissors (choose "exit" to quit): ').lower()

        if player == 'exit':
            print('Thanks for playing!')
            break

        if player not in options:
            print('Invalid choice, please try again')
            continue

        cpu = random.choice(options)

        if player == cpu:
            print("It's a tie!")
        elif winning_options[player] == cpu:
            print("You win!")
        else:
            print("You lose!")

game()

