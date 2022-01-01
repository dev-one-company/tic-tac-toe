from tests.board_repository_test import TestBoardRepository

import unittest

from tests.core_test import TestMatchCases

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestMatchCases("test_match_row"))
    suite.addTest(TestMatchCases("test_match_column"))
    suite.addTest(TestMatchCases("test_match_diagonal_top_left_to_bottom_right"))
    suite.addTest(TestMatchCases("test_diagonal_top_right_to_bottom_left"))
    suite.addTest(TestMatchCases("without_solution"))

    suite.addTest(TestBoardRepository("test_create"))
    suite.addTest(TestBoardRepository("test_get_board"))
    suite.addTest(TestBoardRepository("test_mark_board_position"))

    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite)

    unittest.main()
