class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num = 0
        maxI = len(grid)
        maxJ = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == '1':
                    q = deque()
                    q.append((i, j))
                    visited.add((i, j))
                    while q:
                        for x in range(len(q)):
                            curr = q.popleft()
                            currI = curr[0]
                            currJ = curr[1]
                            if currI + 1 < maxI and grid[currI + 1][currJ] == '1' and (currI + 1, currJ) not in visited:
                                q.append((currI + 1, currJ))
                                visited.add((currI + 1, currJ))
                            if currJ + 1 < maxJ and grid[currI][currJ+1] == '1' and (currI, currJ+1) not in visited:
                                q.append((currI, currJ+1))
                                visited.add((currI, currJ+1))
                            if currI - 1 >= 0 and grid[currI - 1][currJ] == '1' and (currI - 1, currJ) not in visited:
                                q.append((currI - 1, currJ))
                                visited.add((currI - 1, currJ))
                            if currJ - 1 >= 0 and grid[currI][currJ-1] == '1' and (currI, currJ-1) not in visited:
                                q.append((currI, currJ-1))
                                visited.add((currI, currJ-1))
                    num += 1

        return num
        