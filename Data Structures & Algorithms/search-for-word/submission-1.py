class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxI = len(board)
        maxJ = len(board[0])
        def traverse(curr, i, j, x, visited):
            if curr == word:
                return True
            if len(curr) >= len(word):
                return False
            if i+1 < maxI and board[i+1][j] == word[x] and (i+1, j) not in visited:
                if traverse(curr + word[x], i+1, j, x+1, visited | {(i+1, j)}):
                    return True
            if j+1 < maxJ and board[i][j+1] == word[x] and (i, j+1) not in visited:
                if traverse(curr + word[x], i, j+1, x+1, visited | {(i, j+1)}):
                    return True
            if i-1 >= 0 and board[i-1][j] == word[x] and (i-1, j) not in visited:
                if traverse(curr + word[x], i-1, j, x+1, visited | {(i-1, j)}):
                    return True
            if j-1 >= 0 and board[i][j-1] == word[x] and (i, j-1) not in visited:
                if traverse(curr + word[x], i, j-1, x+1, visited | {(i, j-1)}):
                    return True
            return False
        for I in range(len(board)):
            for J in range(len(board[I])):
                if board[I][J] == word[0]:
                    vis = set()
                    vis.add((I, J))
                    if traverse(word[0], I, J, 1, vis):
                        return True
        return False

        