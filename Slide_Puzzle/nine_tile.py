import random
import itertools
"""
the board will have 9 blocks that have a number 1-8 with the 9th block having no number. These
blocks will be arranged in random order in a 3x3 board. the point of the game is to have 
the block numbers in order from 1-8 where 1 starts at the top left and the empty block ends 
in the bottom right
the board will look like this once finished

[
    [1],[2],[3],
    [4],[5],[6],
    [7],[8],[]
]

rules:

1. the blocks can only switch places with the empty block
2. Blocks can only switch with the empty block if it is right next
   to them.
3. game ends when the board is in this format: 
    [1],[2],[3],
    [4],[5],[6],
    [7],[8],[ ]
"""

MBL = 9 # 0 index Maximum Board Length
class Board(object):
    def __init__(self):
        self.empty_space = None
        self.board = self.setup_board()

    def setup_board(self):
        """Creates and populates the board
        
        Returns:
            list[Tile] -- list with MBL x MBL lists each containing a Tile Object
        """
        board_rows = []
        random_nums = random.sample(range(MBL),9)
        for y in range(MBL//3):
            row = []
            for x in range(MBL//3):
                number = random_nums.pop(0)
                if number == 0:
                    self.empty_space =[y,x]
                row.append(Tile(x,y,number))
            board_rows.append(row)
        return board_rows   
   
    def shuffle(self,coordinates):
        """Shuffles the Tile located in the given coordinates
        
        Arguments:
            coordinates [] -- list containing y-coordinate and x-coordinate
        """
        shuffle1, shuffle2 = self.board[self.empty_space[0]][self.empty_space[1]], self.board[coordinates[0]][coordinates[1]]
        self.board[self.empty_space[0]][self.empty_space[1]], self.board[coordinates[0]][coordinates[1]] = shuffle2, shuffle1
        self.empty_space = [coordinates[0],coordinates[1]]
    
    def possible_moves(self):
        """Finds the possible set of moves for the user to select
        
        Returns:
            list -- contains tuple(s) of possible moves with y-coordinate and x-coordinate
        """
        possible_x = []
        possible_y = []
        if 0 < self.empty_space[1]<(MBL//3)-1:
            possible_x.append(self.empty_space[1]+1)
            possible_x.append(self.empty_space[1]-1)
        elif self.empty_space[1] == (MBL//3)-1:
            possible_x.append(self.empty_space[1]-1)
        else:
            possible_x.append(self.empty_space[1]+1)
        if 0 < self.empty_space[0] < (MBL//3)-1:
            possible_y.append(self.empty_space[0]+1)
            possible_y.append(self.empty_space[0]-1)
        elif self.empty_space[0] == (MBL//3)-1:
            possible_y.append(self.empty_space[0]-1)
        else:
            possible_y.append(self.empty_space[0]+1)
        set_of_moves = [(y,self.empty_space[1]) for y in possible_y]
        set_of_moves = set_of_moves + [(self.empty_space[0],x) for x in possible_x]
        return set_of_moves
    
    def finished_game(self, user_end_game = False):
        """Check whether user asked to end game or whether the tiles on the board
        are in the correct order to end the game
        
        Keyword Arguments:
            user_end_game {bool} -- True if user wants to end game (default: {False})
        
        Returns:
            bool -- True if game is in end state or user decided to end game, False to continue game
        """
        if user_end_game == True:
            return True
        else:   
            ordered_tile_nums = [num for num in range(MBL)]
            finished_board = [[ordered_tile_nums.pop(0) for x in range(MBL//3) ] for y in range(MBL//3)]
            for y in range(MBL//3):
                for x in range(MBL//3):
                    tile = self.board[y][x]
                    correct_num = finished_board[y][x]
                    if tile.num != correct_num:
                        return False
            return True

    def print_board(self):
        print('')
        for y in range(MBL//3):
            print(" ".join([str(self.board[x][y]) for x in range(MBL//3)]))
        print("")

class Tile:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num

    def __repr__(self):
        """modifies the print of Tile method to only display '[self.num]' or '[ ]'
        
        Returns:
            string -- representation of the Tile method
        """
        if self.num != 0:
            return "[{}]".format(self.num)
        else:
            return "[ ]"
    


def main():
    b = Board()
    end_game = False
    while not end_game:
        b.print_board()
        moves = b.possible_moves()
        possible_moves = {}
        print('Possible Moves:')
        for move in moves:
            # possible_moves[str(counter)] = move
            tile = b.board[move[0]][move[1]]
            possible_moves[str(tile.num)] = move
            print("\t{0}".format(tile.num))
        user_input = input("Enter number corresponding to tile to move: (or enter 'quit' to end game)\n")
        valid_input = False
        while not valid_input:
            if user_input == 'quit':
                valid_input = True
                end_game = b.finished_game(user_end_game=True)
            elif user_input in possible_moves:
                valid_input = True
                b.shuffle(possible_moves[user_input])
                end_game = b.finished_game()
            else:
                valid_input = False
                user_input = input("Please enter a valid number: (or enter 'end' to end game)\n")


            



    

if __name__ == "__main__":
    main()
    



