#move class

class Move:

    # each move will have a particular value
    # a position on the board
    def __init__(self, value):
        self._value = value # this value is non-public
    
    @property
    # we want to make this read only
    # cannot change this after the move is done
    def value(self):
        return self._value
    
    def is_valid(self):
        # to check if the move is valid
        return 1 <= self._value <= 9
    # will return True if it is within the bound
    # will return False if not in the bound

    # we need the row and the column to locate the move based on the value
    def get_row(self):
        if self._value in (1, 2, 3):
            return 0 # this is the first row on the board
        elif self._value in (4, 5, 6):
            return 1 # this is the second row
        else:
            return 2

    def get_column(self):
        if self._value in (1, 4, 7):
            return 0 # first column on the board
        elif self._value in (2, 5, 8):
            return 1
        else:
            return 2

move = Move(0)
print(move.value)
print(move.is_valid()) # this does not take any argument
move = Move(10)
print(move.value)
print(move.is_valid())
move = Move(8)
print(move.value)
print(move.is_valid())
print(move.get_row())
print(move.get_column())