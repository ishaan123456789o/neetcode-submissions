class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        res = 0
        maxI = len(grid) - 1
        maxJ = len(grid[0]) - 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    q = deque()
                    q.append((i, j))
                    seen.add((i, j))
                    area = 1
                    while q:
                        for _ in range(len(q)):
                            curr = q.popleft()
                            currI = curr[0]
                            currJ = curr[1]
                            if currI + 1 <= maxI and grid[currI+1][currJ] == 1 and (currI+1, currJ) not in seen:
                                area += 1
                                q.append((currI+1, currJ))
                                seen.add((currI+1, currJ))
                            if currI - 1 >= 0 and grid[currI-1][currJ] == 1 and (currI-1, currJ) not in seen:
                                area += 1
                                q.append((currI-1, currJ))
                                seen.add((currI-1, currJ))
                            if currJ + 1 <= maxJ and grid[currI][currJ+1] == 1 and (currI, currJ+1) not in seen:
                                area += 1
                                q.append((currI, currJ+1))
                                seen.add((currI, currJ+1))
                            if currJ - 1 >= 0 and grid[currI][currJ-1] == 1 and (currI, currJ-1) not in seen:
                                area += 1
                                q.append((currI, currJ-1))
                                seen.add((currI, currJ-1))
                    res = max(res, area)
        return res
        