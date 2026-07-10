class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        maxI = len(heights)-1
        maxJ = len(heights[0])-1
        i = 0
        for j in range(len(heights[i])):
            if (i, j) not in pacific:
                q = deque()
                q.append((i, j))
                pacific.add((i, j))
                while q:
                    for _ in range(len(q)):
                        curr = q.popleft()
                        currI = curr[0]
                        currJ = curr[1]
                        if currI + 1 <= maxI and heights[currI + 1][currJ] >= heights[currI][currJ] and (currI + 1, currJ) not in pacific:
                            q.append((currI + 1, currJ))
                            pacific.add((currI + 1, currJ))
                        if currJ + 1 <= maxJ and heights[currI][currJ+1] >= heights[currI][currJ] and (currI, currJ + 1) not in pacific:
                            q.append((currI, currJ+1))
                            pacific.add((currI, currJ+1))
                        if currI - 1 >= 0 and heights[currI - 1][currJ] >= heights[currI][currJ] and (currI - 1, currJ) not in pacific:
                            q.append((currI - 1, currJ))
                            pacific.add((currI - 1, currJ))
                        if currJ - 1 >= 0 and heights[currI][currJ - 1] >= heights[currI][currJ] and (currI, currJ - 1) not in pacific:
                            q.append((currI, currJ-1))
                            pacific.add((currI, currJ-1))
        j = 0
        for i in range(len(heights)):
            if (i, j) not in pacific:
                q = deque()
                q.append((i, j))
                pacific.add((i, j))
                while q:
                    for _ in range(len(q)):
                        curr = q.popleft()
                        currI = curr[0]
                        currJ = curr[1]
                        if currI + 1 <= maxI and heights[currI + 1][currJ] >= heights[currI][currJ] and (currI + 1, currJ) not in pacific:
                            q.append((currI + 1, currJ))
                            pacific.add((currI + 1, currJ))
                        if currJ + 1 <= maxJ and heights[currI][currJ+1] >= heights[currI][currJ] and (currI, currJ + 1) not in pacific:
                            q.append((currI, currJ+1))
                            pacific.add((currI, currJ+1))
                        if currI - 1 >= 0 and heights[currI - 1][currJ] >= heights[currI][currJ] and (currI - 1, currJ) not in pacific:
                            q.append((currI - 1, currJ))
                            pacific.add((currI - 1, currJ))
                        if currJ - 1 >= 0 and heights[currI][currJ - 1] >= heights[currI][currJ] and (currI, currJ - 1) not in pacific:
                            q.append((currI, currJ-1))
                            pacific.add((currI, currJ-1))

        i = maxI
        for j in range(len(heights[i])):
            if (i, j) not in atlantic:
                q = deque()
                q.append((i, j))
                atlantic.add((i, j))
                while q:
                    for _ in range(len(q)):
                        curr = q.popleft()
                        currI = curr[0]
                        currJ = curr[1]
                        if currI + 1 <= maxI and heights[currI + 1][currJ] >= heights[currI][currJ] and (currI + 1, currJ) not in atlantic:
                            q.append((currI + 1, currJ))
                            atlantic.add((currI + 1, currJ))
                        if currJ + 1 <= maxJ and heights[currI][currJ+1] >= heights[currI][currJ] and (currI, currJ + 1) not in atlantic:
                            q.append((currI, currJ+1))
                            atlantic.add((currI, currJ+1))
                        if currI - 1 >= 0 and heights[currI - 1][currJ] >= heights[currI][currJ] and (currI - 1, currJ) not in atlantic:
                            q.append((currI - 1, currJ))
                            atlantic.add((currI - 1, currJ))
                        if currJ - 1 >= 0 and heights[currI][currJ - 1] >= heights[currI][currJ] and (currI, currJ - 1) not in atlantic:
                            q.append((currI, currJ-1))
                            atlantic.add((currI, currJ-1))
        j = maxJ
        for i in range(len(heights)):
            if (i, j) not in atlantic:
                q = deque()
                q.append((i, j))
                atlantic.add((i, j))
                while q:
                    for _ in range(len(q)):
                        curr = q.popleft()
                        currI = curr[0]
                        currJ = curr[1]
                        if currI + 1 <= maxI and heights[currI + 1][currJ] >= heights[currI][currJ] and (currI + 1, currJ) not in atlantic:
                            q.append((currI + 1, currJ))
                            atlantic.add((currI + 1, currJ))
                        if currJ + 1 <= maxJ and heights[currI][currJ+1] >= heights[currI][currJ] and (currI, currJ + 1) not in atlantic:
                            q.append((currI, currJ+1))
                            atlantic.add((currI, currJ+1))
                        if currI - 1 >= 0 and heights[currI - 1][currJ] >= heights[currI][currJ] and (currI - 1, currJ) not in atlantic:
                            q.append((currI - 1, currJ))
                            atlantic.add((currI - 1, currJ))
                        if currJ - 1 >= 0 and heights[currI][currJ - 1] >= heights[currI][currJ] and (currI, currJ - 1) not in atlantic:
                            q.append((currI, currJ-1))
                            atlantic.add((currI, currJ-1))
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i, j) in atlantic and (i, j) in pacific:
                    res.append([i, j])
        return res
        