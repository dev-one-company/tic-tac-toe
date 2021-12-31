from typing import List

class MatchCase(object):
    def __init__(self, board=[]) -> None:
        super().__init__()

        if (len(board) != 3):
            raise ValueError("The board length must be 3")

        for i in range(len(board)):
            if (len(board[i]) != 3):
                raise ValueError(f"The board at position {i} must have length equal to 3")

        self.board = board
        self.boardLength = len(board)

    def match_row(self, findFor) -> int | None:
        """returns the index of matched row or None if not match any row"""


        for i in range(self.boardLength):
            matchCount = 0
            currentRowIndex = i
            for j in range(len(self.board[i])):
                if self.board[i][j] != findFor:
                    break
                else:
                    matchCount += 1
            
            if matchCount == 3:
                return currentRowIndex

        return None


