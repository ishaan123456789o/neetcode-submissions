class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        imax = len(heights)
        jmax = len(heights[0])
        outlook = []
        seen = set()
        seen.add((0, 0))
        if 1 < imax:
            heapq.heappush(outlook, (abs(heights[0][0]-heights[1][0]), 1, 0))
        if 1 < jmax:
            heapq.heappush(outlook, (abs(heights[0][0]-heights[0][1]), 0, 1))
        res = 0
        while outlook:
            current = heapq.heappop(outlook)
            while (current[1], current[2]) in seen:
                current = heapq.heappop(outlook)
            res = max(current[0], res)
            if current[1] == imax-1 and current[2] == jmax-1:
                break
            i = current[1]
            j = current[2]
            seen.add((i,j))
            if i+1 < imax and (i+1, j) not in seen:
                heapq.heappush(outlook, (abs(heights[i+1][j]-heights[i][j]), i+1, j))
            if j+1 < jmax and (i, j+1) not in seen:
                heapq.heappush(outlook, (abs(heights[i][j+1]-heights[i][j]), i, j+1))
            if i-1 >= 0 and (i-1, j) not in seen:
                heapq.heappush(outlook, (abs(heights[i-1][j]-heights[i][j]), i-1, j))
            if j-1 >= 0 and (i, j-1) not in seen:
                heapq.heappush(outlook, (abs(heights[i][j-1]-heights[i][j]), i, j-1))
        return res
        