import unittest

from core import match_cases

board1 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 0]
]
board2 = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 1, 0]
]
board3 = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]
board4 = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 1, 0]
]

class TestMatchCases(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)

    def test_match_row(self):
        match = match_cases.MatchCase(board1)
        self.assertEqual(match.match_row(1), 0)
        
        match = match_cases.MatchCase(board2)
        self.assertEqual(match.match_row(0), 1)

        match = match_cases.MatchCase(board3)
        self.assertEqual(match.match_row(0), 2)

        match = match_cases.MatchCase(board4)
        self.assertEqual(match.match_row(1), None)

        match = match_cases.MatchCase(board4)
        self.assertEqual(match.match_row(0), None)


if __name__ == '__main__':
    unittest.main()