import os
file_path  = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.abspath(os.path.join(file_path, os.pardir))
code_path = dir_path + "\\Slide_Puzzle"
import sys
sys.path.append(code_path)
import unittest
from unittest.mock import patch,MagicMock
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



if __name__ == "__main__":
    unittest.main()