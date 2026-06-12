class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxI = len(matrix)
        maxJ = len(matrix[0])
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                memo[(i, j)] = 1
                if i + 1 < maxI and matrix[i+1][j] > matrix[i][j]:
                    memo[(i, j)] = max(memo[(i, j)], 1 + dp(i+1, j))
                if j + 1 < maxJ and matrix[i][j+1] > matrix[i][j]:
                    memo[(i, j)] = max(memo[(i, j)], 1 + dp(i, j+1))
                if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                    memo[(i, j)] = max(memo[(i, j)], 1 + dp(i-1, j))
                if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                    memo[(i, j)] = max(memo[(i, j)], 1 + dp(i, j-1))
            return memo[(i, j)]
        res = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                res = max(res, dp(x, y))
        return res
        