class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        maxi = len(obstacleGrid)
        maxj = len(obstacleGrid[0])
        memo = {}
        def dp(i, j):
            if i >= maxi or j >= maxj or obstacleGrid[i][j] == 1:
                return 0
            if i == maxi-1 and j == maxj-1:
                return 1
            if (i, j) not in memo:
                memo[(i,j)] = dp(i+1, j) + dp(i, j+1)
            return memo[(i,j)]
        return dp(0, 0)
        