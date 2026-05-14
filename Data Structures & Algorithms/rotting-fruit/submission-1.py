class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxI = len(grid)
        maxJ = len(grid[0])
        time = -1
        q = deque()
        numFresh = 0
        for i in range(maxI):
            for j in range(maxJ):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    numFresh += 1
        if numFresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                i = curr[0]
                j = curr[1]
                if i + 1 < maxI and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1, j))
                if j + 1 < maxJ and grid[i][j+1] == 1:
                    grid[i][j+1] = 2 
                    q.append((i, j+1))
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1, j))
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append((i, j-1))
            time += 1
        for i in range(maxI):
            for j in range(maxJ):
                if grid[i][j] == 1:
                    return -1
        return time
            


        