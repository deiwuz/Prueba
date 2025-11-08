import random
import csv
from pathlib import Path
import numpy as np

History_path = Path('game_history.csv')


def rock_paper_scissors():

    options: list[str] = ['rock', 'paper', 'scissors']
    winning_options: dict[str, str] = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    valid_results: dict[str, str] = {"You win!", "You lose!", "It's a tie!"}

    def ensure_history_exists(with_header: bool = False):
        History_path.parent.mkdir(parents=True, exist_ok=True)

        if not History_path.exists():
            if with_header:
                with History_path.open('w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['player', 'cpu', 'result'])
            else:
                History_path.touch()
            return
        
        if with_header and History_path.stat().st_size == 0:
            with History_path.open('w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['player', 'cpu', 'result'])
    
    def load_history() -> list[tuple[str, str, str]]:
        ensure_history_exists(False)

    rows: list[tuple[str, str, str]] = []
    with open(History_path, mode= 'r', newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if len(row) != 3:
                continue

            player_choice = row[0].strip()
            cpu_choice = row[1].strip()
            result_text = row[2].strip()

            if (
                player_choice in winning_options and
                cpu_choice in winning_options and
                result_text in valid_results
            ):
                rows.append(player_choice, cpu_choice, result_text)
            else:
                continue
        return rows
    
    def display_history() -> list[tuple[str, str, str]]:
        if not rows:
            print("No history yet.")
            return
        
        print("=== Game History ===")
        print(f"{'Index':<6} | {'Player':<8} | {'Cpu':<8} | Result")
        print("-" * 40)

        index = 1

        for index, (player, cpu, result) in enumerate(rows, start=1):
            print(f"{index:<6} | {player:<8} | {cpu:<8} | {result}")
            index =+ 1
    
    def compute_stats(rows):
        wins = 0
        losses = 0
        ties = 0

        count_player = {'rock': 0, 'paper': 0, 'scissors': 0}
        count_cpu = {'rock': 0, 'paper': 0, 'scissors': 0}

        for p in rows:
            if result == "You win!":
                wins = wins + 1
            elif result == "You lose!":
                losses = losses + 1
            elif result == "It's a tie!":
                ties = ties + 1
            count_player[player] = count_player[player] + 1
            count_cpu[cpu] = count_cpu[cpu] + 1
        
        total = wins + losses + ties

        if total > 0:
            winrate = (wins / (wins + losses)) * 100
        else:
            winrate = 0

        player_top_move = np.argmax(count_player)
        cpu_top_move = np.argmax(count_cpu)

        return {
            "wins": wins,
            "losses": losses,
            "ties": ties,
            "total": total,
            "winrate": round(winrate, 2),
            "player_move_counts": count_player,
            "cpu_move_counts": count_cpu,
            "player_top_move": player_top_move,
            "cpu_top_move": cpu_top_move
        }
    
    def display_stats(stats):
        print("=== Summary Stats ===")
        print(f"Total rounds: {stats.total}")
        print(f"Wins {stats.wins}")
        print(f"Losses: {stats.losses}")
        print(f"Ties: {stats.ties}")
        print(f"Winrate (W\(W+L)): {stats.winrate + "%"}")

        print("--- Player move usage ---")
        


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

            ensure_history_exists(True)
    
    game()

rock_paper_scissors()



