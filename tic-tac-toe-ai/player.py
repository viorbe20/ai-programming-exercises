import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'Turno de {self.letter}. Introduce un número de 0 a 8: ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Casilla incorrecta. Inténtalo de nuevo.')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # If all squares are available, choose one randomly
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else: # get a square based on minimax algorythm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        # state = state of the game in a specific moment
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'
        
        # checking if the previous move is a winner
        # Utility function (score): element1 (1(X) or -1(O) or (0)tile) * element2 = empty squares + 1
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares(): 
            return {'position': None,'score': 0}
        
        # define best which is saving the best position for the next move and the best score
        if player == max_player:
            best =  {'position': None, 'score': -math.inf}  # score obtains the maximum score
        else:
            best = {'position': None,'score': math.inf}  # each score obtains the minimum score
        
        # iterates for each possible move and saves the best position
        for possible_move in state.available_moves():
            # try first move
            state.make_move(possible_move, player)
            
            # recurse using minimax to simulate a game after making that move
            # players alternation
            sim_score = self.minimax(state, other_player)
            
            # undo the move and reset the move
            state.board[possible_move] = ' ' 
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # is necessary, update the dictionary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best