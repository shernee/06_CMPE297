import unittest
from unittest.mock import patch
from io import StringIO
import wordle

class TestWordle(unittest.TestCase):
    @patch('wordle.input', return_value='grape')
    @patch('wordle.datetime.now')
    def test_wordle_game_correct_guess(self, mock_datetime, mock_input):
        mock_datetime.return_value.day = 1
        with patch('sys.stdout', new=StringIO()) as fake_out:
            wordle.wordle_game()
            self.assertIn("Congratulations! You've guessed the word in 1 attempts.", fake_out.getvalue().strip())

    @patch('wordle.input', return_value='grape')
    @patch('wordle.datetime.now')
    def test_wordle_game_incorrect_guess(self, mock_datetime, mock_input):
        mock_datetime.return_value.day = 1
        with patch('sys.stdout', new=StringIO()) as fake_out:
            wordle.wordle_game()
            self.assertIn("Please enter a 5-letter word.", fake_out.getvalue().strip())

if __name__ == '__main__':
    unittest.main()