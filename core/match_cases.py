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

    def match_row(self, match) -> int | None:
        """returns the index of matched row or None if not match any row"""

        for i in range(self.boardLength):
            matchCount = 0
            for j in range(self.boardLength):
                if self.board[i][j] != match:
                    break
                else:
                    matchCount += 1
            
            if matchCount == 3:
                return i

        return None

    def match_column(self, match) -> int | None:
        """returns the index of matched column or None if not match any row"""

        for i in range(self.boardLength):
            matchCount = 0
            for j in range(self.boardLength):
                if self.board[j][i] != match:
                    break
                else:
                    matchCount += 1
            
            if matchCount == self.boardLength:
                return i

        return None

    def diagonal_top_left_to_bottom_right(self, match) -> bool:
        for i in range(self.boardLength):
            if self.board[i][i] != match:
                return False

        return True
    
    def diagonal_top_right_to_bottom_left(self, match) -> bool:
        for i in range(self.boardLength):
            if self.board[i][self.boardLength - 1 - i] != match:
                return False
        
        return True

