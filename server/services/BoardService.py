from server.repositories.Board import Board
from server.core.match_cases import MatchCase


class BoardService:
    def __init__(self, board_id: str):
        self.board_id = board_id
        self.board = Board()

    def check_match(self, player) -> dict | None:

        game_board = self.board.get_board(self.board_id)
        match_cases = MatchCase(game_board)

        match_row = match_cases.match_row(player)
        if match_row is not None:
            return {
                'name': 'ROW MATCH',
                'pos': match_row
            }

        match_column = match_cases.match_column(player)
        if match_column is not None:
            return {
                'name': 'COLUMN MATCH',
                'pos': match_column
            }

        diagonal_top_left_to_bottom_right = match_cases.diagonal_top_left_to_bottom_right(player)
        if diagonal_top_left_to_bottom_right:
            return {
                'name': 'DIAGONAL MATCH',
                'pos': 0
            }

        diagonal_top_right_to_bottom_left = match_cases.diagonal_top_right_to_bottom_left(player)
        if diagonal_top_right_to_bottom_left:
            return {
                'name': 'DIAGONAL MATCH',
                'pos': 2
            }

        return None

    def is_without_solution(self):
        board = self.board.get_board(self.board_id)
        match_cases = MatchCase(board)

        if match_cases.without_solution():
            self.board.delete_board(self.board_id)
            return True

        return False
