import time
import tkinter as tk
from tkinter import messagebox
from player import HumanPlayer, GeniusComputerPlayer

class TicTacToe:
    '''
    Instance of TicTacToe with an empty board and without a winner
    It establishes board size
    '''
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    # '''
    # Print current board state (a list of nine) iterating thorugh each row
    # '''
    # def print_board(self):
    #     for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
    #         print('| ' + ' | ' .join(row) + ' |')

    # @staticmethod
    # def print_board_nums():
    #     # print initial board with the number of squares
    #     number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]

    #     # print numbers inside the 3x3 board
    #     for row in number_board:
    #         print('| ' + ' | ' .join(row) + ' |')

    def available_moves(self):
        # returns a list with indexes from empty squares on the board
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # check if there are empty squares on the board and returns True if so
        return ' ' in self.board

    def num_empty_squares(self):
        # returns the exact number of empty squares on the board
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if a valid move, assign the square to the letter and return True. If not, return False
        if self.board[square] == ' ':
            self.board[square] = letter

            # check if someone won
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check all the possibilities of 3 in a row

        # checking the row
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # checking the column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Only if it is an even number, can it be a diagonal
        if square % 2 == 0:

            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left
            if all([spot == letter for spot in diagonal2]):
                return True

        # if there is no winner
        return False

class TicTacToeGUI:
    def __init__(self, game):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.game = game

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('normal', 20), width=8, height=4,
                                              command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.game.board[row * 3 + col] == ' ' and not self.game.current_winner:
            self.game.make_move(row * 3 + col, 'X')
            self.buttons[row][col].config(text='X')

            if self.game.current_winner:
                winner = self.game.current_winner
                messagebox.showinfo(f"{winner} wins!")
                self.reset_game()

            elif not self.game.empty_squares():
                messagebox.showinfo("Tic Tac Toe", "¡Empate!")
                self.reset_game()

            else:
                # Computer's move
                self.root.after(1000, self.computer_move)

    def computer_move(self):
        if not self.game.current_winner:
            square = o_player.get_move(self.game)
            self.game.make_move(square, 'O')
            row, col = divmod(square, 3)
            self.buttons[row][col].config(text='O')

            if self.game.current_winner:
                winner = self.game.current_winner
                messagebox.showinfo(f"¡Ha ganado {winner}!")
                self.reset_game()

            elif not self.game.empty_squares():
                messagebox.showinfo("¡Empate!")
                self.reset_game()

    def reset_game(self):
        self.game.__init__()

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    t = TicTacToe()
    o_player = GeniusComputerPlayer('O')
    gui = TicTacToeGUI(t)
    gui.run()
