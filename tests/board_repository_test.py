from typing import List

from server.repositories.Board import Board
import unittest

board_id = ""


class TestBoardRepository(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.board = Board()

    def test_a_create(self):
        global board_id
        board_id = self.board.create()

        self.assertIsNotNone(board_id)

    def test_b_get_board(self):
        board = self.board.get_board(board_id)

        self.assertEqual(len(board), 3)

        for i in range(3):
            for j in range(3):
                self.assertIsNone(board[j][i])

    def test_c_mark_board_position(self):
        self.board.mark_board_position(0, 0, board_id, 1)
        self.board.mark_board_position(2, 0, board_id, 1)
        self.board.mark_board_position(0, 2, board_id, 0)

        board = self.board.get_board(board_id)

        self.assertEqual(board[0][0], 1)
        self.assertEqual(board[0][2], 0)
        self.assertEqual(board[2][0], 1)

    def test_d_delete_board(self):
        self.board.delete_board(board_id)

        try:
            board = self.board.get_board(board_id)
            self.assertNotIsInstance(board, List)
        except Exception as e:
            self.assertEqual(str(e), "This board not exist")
