import random

print("===============================")
print("Rock Paper Scissors Lizard Spock")
print("===============================")

Winning_movements = {
'Scissors': ['Lizard', 'Paper'],
'Paper': ['Rock', 'Spock'],
'Rock': ['Lizard', 'Scissors'],
'Lizard': ['Spock', 'Paper'],
'Spock': ['Scissors', 'Rock'],
}

Valid_movements = { 
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors',
    4: 'Lizard',
    5: 'Spock'
}

def Game():
    while True:
        Cpu_movement = random.randint(1, 5)
        try:
            Movement = int(input("1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\n6) Exit\nPick a number: "))

            if Movement == 6:
                print("Leaving the program")
                break

            if Movement not in Valid_movements:
                print("Thats not a valid option, try again.")
                continue

            User_choice = Valid_movements[Movement]
            Cpu_choice = Valid_movements[Cpu_movement]

            if User_choice == Cpu_choice:
                print("Tie, try again.")
                continue
            if Cpu_choice in Winning_movements[User_choice]:
                print("You win!!!")
                continue
            else:
                print("The cpu wins!!!")
                continue
        except ValueError:
            print("Please select a valid option (1,2,3,4,5,6)")

Game()