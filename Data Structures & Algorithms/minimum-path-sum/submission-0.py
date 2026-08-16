class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        imax = len(grid)
        jmax = len(grid[0])
        memo = {}
        def dp(i, j):
            if i == imax-1 and j == jmax-1:
                return grid[imax-1][jmax-1]
            if (i,j) not in memo:
                memo[(i,j)] = float('inf')
                if i+1 < imax:
                    memo[(i,j)] = min(memo[(i,j)], grid[i][j] + dp(i+1, j))
                if j+1 < jmax:
                    memo[(i,j)] = min(memo[(i,j)], grid[i][j] + dp(i, j+1))
            return memo[(i,j)]
        return dp(0, 0)
        