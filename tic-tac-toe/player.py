import random

class Player:
    def __init__(self, letter):
        # letter can be both x and o
        self.letter = letter
        
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # choose an empty random spot on the board
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # human can choose an empty spot on the board
        valid_square = False
        val  = None
        
        # while not valid square, choose an empty spot on the board
        while not valid_square:
            square = input(f'Turno de {self.letter}. Introduce una posición de 0 a 8: ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Posición incorrecta. Inténtalo de nuevo.\n')
        return val