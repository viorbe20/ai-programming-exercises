class TicTacToe:
    def __init__(self):
        # single list for representing 3x3 board
        self.board = ['' for _ in range(9)]
        self.current_winer = None
    
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
        return [i for i, spot in enumerate(self.board) if spot == '']