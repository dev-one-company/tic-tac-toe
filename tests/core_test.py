import unittest

from core import match_cases

matchs = {
    "row": {
        "1": [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 0]
        ],
        "2": [
            [1, 0, 1],
            [0, 0, 0],
            [1, 1, 0]
        ],
        "3": [
            [1, 0, 1],
            [0, 1, 0],
            [0, 0, 0]
        ],
        "4": [
            [1, 0, 1],
            [0, 1, 0],
            [0, 1, 0]
        ]
    },
    "column": {
        "1": [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        "2": [
            [1, 0, 1],
            [0, 0, 1],
            [1, 0, 0]
        ],
        "3": [
            [0, 1, 1],
            [1, 0, 1],
            [0, 0, 1]
        ],
        "4": [
            [1, 0, 1],
            [0, 1, 0],
            [0, 1, 0]
        ]
    },
    "diagonal_top_left_to_bottom_right": {
        "1": [
            [1, 0, 1],
            [1, 1, 0],
            [0, 0, 1]
        ],
        "2": [
            [0, 1, 1],
            [1, 0, 0],
            [0, 1, 0]
        ],
        "3": [
            [0, 0, 1],
            [1, 1, 0],
            [0, 1, 0]
        ],
    },
    "diagonal_top_right_to_bottom_left": {
        "1": [
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 0]
        ],
        "2": [
            [0, 1, 0],
            [1, 0, 0],
            [0, 1, 1]
        ],
        "3": [
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0]
        ],
    },
}


class TestMatchCases(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)

    def test_match_row(self):
        match = match_cases.MatchCase(matchs["row"]["1"])
        self.assertEqual(match.match_row(1), 0)

        match = match_cases.MatchCase(matchs["row"]["2"])
        self.assertEqual(match.match_row(0), 1)

        match = match_cases.MatchCase(matchs["row"]["3"])
        self.assertEqual(match.match_row(0), 2)

        match = match_cases.MatchCase(matchs["row"]["4"])
        self.assertEqual(match.match_row(1), None)

        match = match_cases.MatchCase(matchs["row"]["4"])
        self.assertEqual(match.match_row(0), None)

    def test_match_column(self):
        match = match_cases.MatchCase(matchs["column"]["1"])
        self.assertEqual(match.match_column(1), 0)

        match = match_cases.MatchCase(matchs["column"]["2"])
        self.assertEqual(match.match_column(0), 1)

        match = match_cases.MatchCase(matchs["column"]["3"])
        self.assertEqual(match.match_column(1), 2)

        match = match_cases.MatchCase(matchs["column"]["4"])
        self.assertEqual(match.match_column(1), None)

        match = match_cases.MatchCase(matchs["column"]["4"])
        self.assertEqual(match.match_column(0), None)

    def test_match_diagonal_top_left_to_bottom_right(self):
        match = match_cases.MatchCase(matchs["diagonal_top_left_to_bottom_right"]["1"])
        self.assertEqual(match.diagonal_top_left_to_bottom_right(1), True)

        match = match_cases.MatchCase(matchs["diagonal_top_left_to_bottom_right"]["2"])
        self.assertEqual(match.diagonal_top_left_to_bottom_right(0), True)

        match = match_cases.MatchCase(matchs["diagonal_top_left_to_bottom_right"]["3"])
        self.assertEqual(match.diagonal_top_left_to_bottom_right(0), False)

        match = match_cases.MatchCase(matchs["diagonal_top_left_to_bottom_right"]["3"])
        self.assertEqual(match.diagonal_top_left_to_bottom_right(1), False)

    def test_diagonal_top_right_to_bottom_left(self):
        match = match_cases.MatchCase(matchs["diagonal_top_right_to_bottom_left"]["1"])
        self.assertEqual(match.diagonal_top_right_to_bottom_left(1), True)

        match = match_cases.MatchCase(matchs["diagonal_top_right_to_bottom_left"]["2"])
        self.assertEqual(match.diagonal_top_right_to_bottom_left(0), True)

        match = match_cases.MatchCase(matchs["diagonal_top_right_to_bottom_left"]["3"])
        self.assertEqual(match.diagonal_top_right_to_bottom_left(0), False)

        match = match_cases.MatchCase(matchs["diagonal_top_right_to_bottom_left"]["3"])
        self.assertEqual(match.diagonal_top_right_to_bottom_left(1), False)

