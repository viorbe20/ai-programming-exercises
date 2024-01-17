import time
from player import HumanPlayer, GeniusComputerPlayer

class TicTacToe:
    '''
    Instance of TicTacToe with an empty board and without a winner
    It establishes board size
    '''
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    '''
    Print current board state (a list of nine) iterating thorugh each row
    '''
    def print_board(self):
        print('\n')
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | ' .join(row) + ' |')
    
    '''
    Prints an initial 3x3 board with numbers from 0 to 8.
    Number is a position in the board, providing a visual reference for players.
    '''
    @staticmethod
    def print_board_nums():
        print('\n')
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        
        #print numbers inside the 3x3 board
        for row in number_board:
            print('| ' + ' | ' .join(row) + ' |')
    '''
    Returns a list with indexes from empty squares on the board 
    '''
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    '''
    Returns true if there is, at least, one empty square
    '''
    def empty_squares(self):
        return ' ' in self.board
    
    '''
    Returns the exact number of empty squares on the board
    '''
    def num_empty_squares(self):
        return self.board.count(' ')
    
    '''
    Check if the last move is valid. If valid, update the game board with the symbol.
    Check if the last move results in a new winner. If so, update the winner.
    '''
    def make_move(self, square, letter):
        # if valid move, assign square to letter and return True.
        if self.board[square] == ' ':
            self.board[square] = letter
            
            # check if someone won and if so, update it
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    '''
    Check if the last movement is a winner movement
    '''
    def winner(self, square, letter):
        # check all the posibilities of 3 in row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # checking the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Only if it is a even number, can be a diagonal
        if square % 2 == 0:
            
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if there is no winner
        return False
    
'''
Coordinates the entire gameplay, allowing players to make moves alternately until the game concludes.
Manages the turn-based moves, updates the game board, and checks for a winner or a draw.
'''
def play(game, x_player, o_player, print_game=True):
    # returns the letter of the winner of the game or a tie
    if print_game:
        game.print_board_nums()
    
    # starting letter
    letter = 'X'
    
    # loop while the game has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
    
        # function to make a move
        if game.make_move(square, letter):
        
            if print_game:
                print(f'\nJugador {letter} se mueve a casilla {square}.')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'Ha ganado {letter}.')
                return letter

            # after a move, we need to switch the players
            letter = 'O' if letter == 'X' else 'X'
    
        # pause
        time.sleep(0.8)
    
    if print_game:
        print(f'Ha habido un empate.')
    return None
        
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)