
class Ship:
	def __init__(self,name: str, size: int):
		self.name = name
		self.size = size
		self.positions = []
		self.impacts = 0
	
	def place_ship(self, start_row, start_col, direction, board):
		temporal_positions = []

		if direction == "H":
			if start_col + self.size > len(board[0]):
				return False
			for i in range(self.size):
				if board[start_row][start_col + i] != " ":
					return False
				temporal_positions.append((start_row, start_col + i))
		
		elif direction == "V":
			if start_row + self.size > len(board):
				return False
			for i in range(self.size):
				if board[start_row + i][start_col] != " ":
					return False
				temporal_positions.append((start_row + i, start_col))
		else:
			return False
		
		for r, c in temporal_positions:
			board[r][c] = self.name[0]
		
		self.positions.extend(temporal_positions)
		return True
		
	def hit(self):
		if self.impacts < self.size:
			self.impacts += 1
		return self.impacts == self.size

class Destroyer(Ship):
		def __init__(self):
			super().__init__("Destroyer", 2)

class Submarine(Ship):
		def __init__(self):
			super().__init__("Submarine", 3)

class Battleship(Ship):
		def __init__(self):
			super().__init__("Battleship", 4)

class Player():
	def __init__(self, name: str):
		self.name = name
		self.board = [[" " for _ in range(10)] for _ in range(10)] 
		self.ships = []
		self.hits = [[" " for _ in range(10)] for _ in range(10)] 
	
	def place_ships(self):
		Available_ships = [Destroyer(), Submarine(), Battleship()]
		for ship in Available_ships:
			while True:
				try:
					print(f"colocando {ship.name} ({ship.size})")
					initial_row = int(input("Fila inicial (0-9): "))
					initial_col = int(input("Columna inicial (0-9): "))
					direction = input('Elige una direccion, "H" para horizontal "V" para vertical: ').strip().upper()

					if not (0 <= initial_row <= 9 and 0 <= initial_col < 10):
						print("Coordenadas fuera de rango")
						continue

					if direction not in ("H", "V"):
						print("Direccion invalida, no es H o V")

					if ship.place_ship(initial_row, initial_col, direction, self.board):
							self.ships.append(ship)
							self.print_board(self.board)
							break
					else:
						print("No cabe o se superpone. intenta de nuevo")
				
				except ValueError: print("Entrada invalida usa numeros enteros")

	def print_board(self, board):
		print("   " + " ".join(str(c) for c in range(10)))
		for i, row in enumerate(board):
			print(f"{i:2} " + " ".join(row))
		print()

	def attack(self, opponent):
		 while True:
				try:
					print(f"{self.name.capitalize()} elige una posicion para atacar")
					row = int(input("En que fila deseas atacar: "))
					col = int(input("En que columna deseas atacar: "))

					if not (0 <= row <= 10 and 0 <= col < 10):
						print("posicion invalida")
						continue
					if self.hits[row][col] != " ":
						print("Esta posicion ya ha sido atacada. Elige otra")
					if opponent.board[row][col] == " ":
						print("Agua!!!")
						self.hits[row][col] = "A"
						opponent.board[row][col] = "A"
						break
					else:
						print("Impacto!")
						self.hits[row][col] = "T"
						opponent.board[row][col] = "T"

						for ship in opponent.ships:
							if (row, col) in ship.positions:
								if ship.hit():
									print(f"!Hundido! Has hundido el {ship.name}")
						break

				except ValueError: print ("El valor debe ser un numero Entero")

	def all_ships_sunk(self):
		for ship in self.ships:
			if ship.impacts != ship.size:
				return False
		return True

class BattleshipGame():
	def __init__(self):
		self.player1 = Player("Jugador 1")
		self.player2 = Player("Jugador 2")
	
	def play(self):
		print("Bienvenido al juego de Batalla Naval")
		print("Jugador 1 coloca sus barcos")
		self.player1.place_ships()


		print("Jugador 2 coloca sus barcos")
		self.player2.place_ships()

		jugador_actual = self.player1
		opponent = self.player2

		while True:
			jugador_actual.attack(opponent)

			if opponent.all_ships_sunk():
				print(f"{jugador_actual.name} ha ganado")
				break

board=[[" " for _ in range(10)] for _ in range(10)] 

for row in board:
	print("a".join(row))

game = BattleshipGame() 
game.play()

