# player class
# keep classes on different files
import random
# how to access Move file?
from move import Move

class Player():
    # 2 types of players
    # human and computer

    PLAYER_MARKER = "X" # class constant that can be referred and updated
    COMPUTER_MARKER = "O"

    def __init__(self, is_human = True):
        # by default we have human player
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER
    
    @property
    def is_human(self):
        return self._is_human # only for accessing values
    
    @property
    def marker(self):
        return self._marker # only for accessing values
    
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        while True:
            user_input = int(input("please enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("please enter an integer between 1 and 9.")
        return move
    
    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print("computer move (1-9): ", move.value)
        return move

player = Player() # human player by default
# test instance attribute
print(player.is_human)
print(player.marker)

# test the methods now, the functions you defined
player.get_move()

# or do it this way
move = player.get_move()
print(move.value)

computer_player = Player(False)
print(computer_player.is_human)
print(computer_player.marker)
move = computer_player.get_move()
print(move.value)