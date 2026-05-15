class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        maxI = len(grid)
        maxJ = len(grid[0])
        q = deque()
        for i in range(maxI):
            for j in range(maxJ):
                if grid[i][j] == 0:
                    q.append((i, j))
        dist = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                i = curr[0]
                j = curr[1]
                if i+1 < maxI and grid[i+1][j] != -1 and grid[i+1][j] != 0 and grid[i+1][j] == inf:
                    q.append((i+1, j))
                    grid[i+1][j] = min(grid[i+1][j], dist)
                if i-1 >= 0 and grid[i-1][j] != -1 and grid[i-1][j] != 0 and grid[i-1][j] == inf:
                    q.append((i-1, j))
                    grid[i-1][j] = min(grid[i-1][j], dist)
                if j+1 < maxJ and grid[i][j+1] != -1 and grid[i][j+1] != 0 and grid[i][j+1] == inf:
                    q.append((i, j+1))
                    grid[i][j+1] = min(grid[i][j+1], dist)
                if j-1 >= 0 and grid[i][j-1] != -1 and grid[i][j-1] != 0 and grid[i][j-1] == inf:
                    q.append((i, j-1))
                    grid[i][j-1] = min(grid[i][j-1], dist)
            dist += 1
        


        