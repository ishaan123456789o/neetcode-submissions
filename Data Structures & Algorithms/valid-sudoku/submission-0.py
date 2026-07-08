class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(3):
            for j in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(3):
            for j in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(3, 6):
            for j in range(3):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(6, 9):
            for j in range(3):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(3):
            for i in range(3):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(3):
            for i in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(3):
            for i in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(3, 6):
            for i in range(3):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(3, 6):
            for i in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(3, 6):
            for i in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(6, 9):
            for i in range(3):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(6, 9):
            for i in range(3, 6):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        seen = set()
        for j in range(6, 9):
            for i in range(6, 9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        return True