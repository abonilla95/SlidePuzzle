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

    # @patch(Board, '__init__',return_value=None) as mock_board:
    def test_setup_board(self):
        with patch.object(Board, '__init__', lambda x: None), patch.object(nine_tile,'Tile', return_value=[]):
            b = Board()
            board = b.setup_board()
            test_b = [[[],[],[]],[[],[],[]],[[],[],[]]]
            self.assertEqual(board, test_b)


if __name__ == "__main__":
    unittest.main()