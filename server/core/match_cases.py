class MatchCase(object):
    def __init__(self, board: list) -> None:
        super().__init__()

        if len(board) != 3:
            raise ValueError("The board length must be 3")

        for i in range(len(board)):
            if len(board[i]) != 3:
                raise ValueError(f"The board at position {i} must have length equal to 3")

        self.board = board
        self.boardLength = len(board)

    def match_row(self, match) -> int | None:
        """returns the index of matched row or None if not match any row"""

        for i in range(self.boardLength):
            match_count = 0
            for j in range(self.boardLength):
                if self.board[i][j] != match:
                    break
                else:
                    match_count += 1

            if match_count == 3:
                return i

        return None

    def match_column(self, match) -> int | None:
        """returns the index of matched column or None if not match any row"""

        for i in range(self.boardLength):
            match_count = 0
            for j in range(self.boardLength):
                if self.board[j][i] != match or self.board[j][i] is None:
                    break
                else:
                    match_count += 1

            if match_count == self.boardLength:
                return i

        return None

    def diagonal_top_left_to_bottom_right(self, match) -> bool:
        for i in range(self.boardLength):
            if self.board[i][i] != match or self.board[i][i] is None:
                return False

        return True

    def diagonal_top_right_to_bottom_left(self, match) -> bool:
        for i in range(self.boardLength):
            if self.board[i][self.boardLength - 1 - i] != match or self.board[i][self.boardLength - 1 - i] is None:
                return False

        return True

    def without_solution(self):
        for i in range(self.boardLength):
            for j in range(self.boardLength):
                if self.board[i][j] is None:
                    return False

        def without_player_solution(player) -> bool:
            if (self.match_row(player) is None and
                    self.match_column(player) is None and
                    not self.diagonal_top_left_to_bottom_right(player) and
                    not self.diagonal_top_right_to_bottom_left(player)):
                return True
            return False

        if without_player_solution(1) and without_player_solution(0):
            return True

        return False
