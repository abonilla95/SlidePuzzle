import os
file_path  = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.abspath(os.path.join(file_path, os.pardir))
code_path = dir_path + "\\Slide_Puzzle"
import sys
sys.path.append(code_path)
import unittest
from unittest.mock import patch, MagicMock
import nine_tile
from nine_tile import Board,Tile, MBL


class Test_Board(unittest.TestCase):

    def test_setup_board(self):
        """Test to see if the size of the board that is created is MBL x MBL
        """
        with patch.object(Board, '__init__', lambda x: None), patch.object(nine_tile,'Tile', return_value=[]):
            b = Board()
            board = b.setup_board()
            test_b = [[[] for y in range(MBL//3)] for x in range(MBL//3)]
            self.assertEqual(board, test_b)

    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_top_left(self):
        b = Board()
        b.empty_space = [0,0]
        result = set(b.possible_moves())
        possible_moves = set([(0,1),(1,0)])
        self.assertEqual(result,possible_moves)

    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_botom_left(self):
        b = Board()
        b.empty_space = [2,0]
        result = set(b.possible_moves())
        possible_moves = set([(1,0),(2,1)])
        self.assertEqual(result,possible_moves)

    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_top_right(self):
        b = Board()
        b.empty_space = [0,2]
        result = set(b.possible_moves())
        possible_moves = set([(0,1),(1,2)])
        self.assertEqual(result,possible_moves)

    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_botom_right(self):
        b = Board()
        b.empty_space = [2,2]
        result = set(b.possible_moves())
        possible_moves = set([(1,2),(2,1)])
        self.assertEqual(result,possible_moves)

    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_center(self):
        b = Board()
        b.empty_space = [1,1]
        result = set(b.possible_moves())
        possible_moves = set([(0,1),(2,1),(1,0),(1,2)])
        self.assertEqual(result,possible_moves)

    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_top_center(self):
        b = Board()
        b.empty_space = [0,1]
        result = set(b.possible_moves())
        possible_moves = set([(0,0),(0,2),(1,1)])
        self.assertEqual(result, possible_moves)
    
    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_bottom_center(self):
        b = Board()
        b.empty_space = [2,1]
        result = set(b.possible_moves())
        possible_moves = set([(2,0),(1,1),(2,2)])
        self.assertEqual(result, possible_moves)

    @patch.object(Board, '__init__', lambda x: None)
    def test_possible_moves_left_center(self):
        b = Board()
        b.empty_space = [1,0]
        result = set(b.possible_moves())
        possible_moves = set([(0,0),(1,1),(2,0)])
        self.assertEqual(result, possible_moves)

    @patch.object(Board, '__init__', lambda x: None)    
    def test_possible_moves_right_center(self):
        b = Board()
        b.empty_space = [1,2]
        result = set(b.possible_moves())
        possible_moves = set([(0,2),(1,1),(2,2)])
        self.assertEqual(result, possible_moves)

    @patch.object(Board,'__init__', lambda x: None)
    def test_finished_game_by_board(self):
        b = Board()
        ordered_tile_nums = [num for num in range(MBL)]
        test_board = []
        for y in range(MBL//3):
            row = []
            for x in range(MBL//3):
                Tile = MagicMock()
                Tile.num = ordered_tile_nums.pop(0)
                row.append(Tile)
            test_board.append(row)
        b.board = test_board
        ending_game = b.finished_game()
        self.assertEqual(ending_game, True)

    @patch.object(Board, '__init__', lambda x: None)
    def test_finished_game_by_user(self):
        b = Board()
        end_game = b.finished_game(user_end_game=True)
        self.assertEqual(end_game, True)

    @patch.object(Board, '__init__', lambda x: None)
    @patch.object(Tile, '__init__', lambda x: None)
    def test_shuffle_board_result(self):
        b = Board()
        b.empty_space = [0,0]
        ordered_tiles = [t for t in range(MBL)]
        b.board = []
        for y in range(MBL//3):
            row = []
            for x in range(MBL//3):
                row.append(ordered_tiles.pop(0))
            b.board.append(row)
        test_board = [[1,0,2],[3,4,5],[6,7,8]]
        b.shuffle([0,1])
        self.assertEqual(b.board,test_board) 

    @patch.object(Board, '__init__', lambda x: None)
    @patch.object(Tile, '__init__', lambda x: None)
    def test_shuffle_empty_space_result(self):
        b = Board()
        b.empty_space = [0,0]
        ordered_tiles = [t for t in range(MBL)]
        b.board = []
        for y in range(MBL//3):
            row = []
            for x in range(MBL//3):
                row.append(ordered_tiles.pop(0))
            b.board.append(row)
        test_board = [[1,0,2],[3,4,5],[6,7,8]]
        test_empty_space = [0,1]
        b.shuffle([0,1])
        self.assertEqual(b.empty_space,test_empty_space)
        
if __name__ == "__main__":
    unittest.main()