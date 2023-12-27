import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        # single list for representing 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        # print a ||| 3x3 board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | ' .join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # number_board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        
        #print numbers insede the 3x3 board
        for row in number_board:
            print('| ' + ' | ' .join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        # check if there are empty squares on the board and returns True if so
        return ' ' in self.board
    
    def num_empty_squares(self):
        # returns the exact number of empty squares on the board
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, assign square to letter and return True. If not, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            
            # check if someone won
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # check all the posibilities of 3 in row
        
        # checking the row
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

def play(game, x_player, o_player, print_game=True):
    # returns the letter of the winner of the game or a tie
    if print_game:
        game.print_board_nums()
    
    # starting letter
    letter = 'X'
    
    # iterates while the game has empty squares
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
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)