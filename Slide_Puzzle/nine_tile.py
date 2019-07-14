import random
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
3. 
"""

MBL = 9 # 0 index Maximum Board Length
class Board(object):
    def __init__(self):
        self.board = self.setup_board()

    def setup_board(self):
        board_rows = []
        random_nums = random.sample(range(MBL),9)
        for x in range(MBL//3):
            row = []
            for y in range(MBL//3):
                row.append(Tile(x,y,random_nums.pop(0)))
            board_rows.append(row)
        return board_rows

    @staticmethod
    def shuffle(tile1,tile2):
        pass

    
    def possible_moves(self):
        pass

    def start_game(self):
        pass
    
    def end_game(self):
        pass

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
        return "[{}]".format(self.num)





    

if __name__ == "__main__":
    b = Board()
    b.print_board()
    



