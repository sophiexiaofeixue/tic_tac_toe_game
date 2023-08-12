# board class
# testing game over
from move import Move
from player import Player

class Board:
    # inital the board is empty

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0], 
                           [0, 0, 0], 
                           [0, 0, 0]]
        # represent each row on the board
        # each row has 3 columns
        # this is the initial representation
        # that is why it is in the __init__
    
    # we need to print out the board
    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()

        print("Board:")
        for row in self.game_board:
            print("|", end = "")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end = "")
                else:
                    print(f" {column} |", end = "")
            print() # print a new line here
        print() # print a new line here

    
    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
        # this is the initial board
    
    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col] 

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("this position is taken. please enter another one.")
    
    def check_is_game_over(self, player, last_move):
        return((self.check_row(player, last_move))
                or (self.check_column(player, last_move)) 
                or (self.check_diagonal(player)) 
                or (self.check_antidiagonal(player)))
    
    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index] # ["O", 0, "X"] for example

        return board_row.count(player.marker) == 3 # count how many X or O
    
    def check_column(self, player, last_move):
        # but column is not a list
        # so we cannot mirror the row method
        markers_count = 0

        col_index = last_move.get_column()
        
        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                markers_count += 1
        return markers_count == 3
    
    def check_diagonal(self, player): # we know the exact location
        # no need to take in the last move
        markers_count = 0

        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1
        return markers_count == 3
    
    def check_antidiagonal(self, player):
        markers_count = 0

        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1
        return markers_count == 3

# we need player and move module
board = Board()
player = Player()
board.print_board()

# need to fill the board 3 times
move_1 = player.get_move()
move_2 = player.get_move()
move_3 = player.get_move()

board.submit_move(player, move_1)
board.print_board()
board.submit_move(player, move_2)
board.print_board()
board.submit_move(player, move_3)
board.print_board()

print(board.check_is_game_over(player, move_3))