
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
            square = self.minimax(game, self.letter)
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


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        
        # If all squares are available, choose one randomly
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # Get available squares with minimax algorythm
            #square = self.minimax(game, self.letter)['position']
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        # state = state of the game in a specific moment
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # checking if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best