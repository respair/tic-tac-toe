"""unittest for tic-tac-toe"""
import io
import unittest
from mock import patch
from XOConsole import XOConsole


class TestXOConsole(unittest.TestCase):
    """tests for the XOConsole class"""

    def setUp(self):
        """instantiating a class"""
        self.tictac = XOConsole()

    @patch('XOConsole.get_input')
    def test_move_x(self, mock_input):
        """check of 1 move"""
        mock_input.return_value = '5'
        self.tictac.move()
        self.assertEqual(self.tictac.board[4], 'X')

    @patch('XOConsole.get_input')
    def test_move_o(self, mock_input):
        """check of 2 moves"""
        mock_input.return_value = '3'
        self.tictac.move()
        mock_input.return_value = '4'
        self.tictac.move()
        self.assertEqual(self.tictac.board[3], 'O')

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    @patch('XOConsole.get_input')
    def test_move(self, mock_input, mock_game, mock_output):
        """check of all moves"""
        test_board = ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O']
        mock_input.return_value = '1'
        self.tictac.move()
        mock_input.return_value = '2'
        self.tictac.move()
        mock_input.return_value = '5'
        self.tictac.move()
        mock_input.return_value = '3'
        self.tictac.move()
        mock_input.return_value = '6'
        self.tictac.move()
        mock_input.return_value = '4'
        self.tictac.move()
        mock_input.return_value = '7'
        self.tictac.move()
        mock_input.return_value = '9'
        self.tictac.move()
        mock_input.return_value = '8'
        self.tictac.move()
        for i in range(9):
            self.assertEqual(self.tictac.board[i], test_board[i])

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_x1(self, mock_new_game, mock_stdout):
        """check win of X"""
        self.tictac.board = ['X', 'O', 'O', 'X', 'X', 'O', 'X', 'O', '9']
        self.tictac.check_win()
        self.assertEqual(mock_stdout.getvalue(), "X is WINNER!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_x2(self, mock_new_game, mock_stdout):
        """checking the call to the new_game function"""
        self.tictac.board = ['X', 'O', 'O', 'X', 'X', 'O', 'X', 'O', '9']
        self.tictac.check_win()
        mock_new_game.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_x1_str(self, mock_new_game, mock_stdout):
        """check win of X"""
        self.tictac.board = ['X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', '9']
        self.tictac.check_win()
        self.assertEqual(mock_stdout.getvalue(), "X is WINNER!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_x2_str(self, mock_new_game, mock_stdout):
        """checking the call to the new_game function"""
        self.tictac.board = ['X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', '9']
        self.tictac.check_win()
        mock_new_game.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_x1_diag(self, mock_new_game, mock_stdout):
        """check win of X"""
        self.tictac.board = ['X', '2', 'O', 'O', 'X', 'X', 'O', '8', 'X']
        self.tictac.check_win()
        self.assertEqual(mock_stdout.getvalue(), "X is WINNER!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_x2_diag(self, mock_new_game, mock_stdout):
        """checking the call to the new_game function"""
        self.tictac.board = ['X', '2', 'O', 'O', 'X', 'X', 'O', '8', 'X']
        self.tictac.check_win()
        mock_new_game.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_o1(self, mock_new_game, mock_stdout):
        """check win of O"""
        self.tictac.board = ['O', 'O', 'O', 'X', 'X', 'O', 'X', '8', '9']
        self.tictac.sign = 'O'
        self.tictac.check_win()
        self.assertEqual(mock_stdout.getvalue(), "O is WINNER!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_o2(self, mock_new_game, mock_stdout):
        """checking the call to the new_game function"""
        self.tictac.board = ['O', 'O', 'O', 'X', 'X', 'O', 'X', 'O', '9']
        self.tictac.sign = 'O'
        self.tictac.check_win()
        mock_new_game.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_nothing1(self, mock_new_game, mock_stdout):
        """check for a draw"""
        self.tictac.board = ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O']
        self.tictac.check_win()
        self.assertEqual(mock_stdout.getvalue(), "НИЧЬЯ!\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.new_game')
    def test_check_win_nothing2(self, mock_new_game, mock_stdout):
        """checking the call to the new_game function"""
        self.tictac.board = ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O']
        self.tictac.check_win()
        mock_new_game.assert_called_once()

    @patch('XOConsole.get_input', return_value='yes')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('XOConsole.XOConsole.main')
    def test_new_game1(self, mock_main, mock_stdout, mock_input):
        """checking the call to the main function"""
        self.tictac.new_game()
        mock_main.assert_called_once()
