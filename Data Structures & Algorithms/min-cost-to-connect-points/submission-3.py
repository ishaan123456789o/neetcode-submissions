class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            abs1 = abs(p1[0]-p2[0])
            abs2 = abs(p1[1]-p2[1])
            return abs1 + abs2
        thePoints = {}
        adjList = defaultdict(list)
        num = 1
        for point in points:
            thePoints[tuple(point)] = num
            num += 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                adjList[thePoints[tuple(points[i])]].append((dist(points[i], points[j]), thePoints[tuple(points[j])]))
                adjList[thePoints[tuple(points[j])]].append((dist(points[i], points[j]), thePoints[tuple(points[i])]))

        seen = set()
        outlook = adjList[1]
        seen.add(1)
        res = 0
        heapq.heapify(outlook)
        while len(seen) < len(points):
            curr = heapq.heappop(outlook)
            while curr[1] in seen:
                curr = heapq.heappop(outlook)
            res += curr[0]
            for item in adjList[curr[1]]:
                heapq.heappush(outlook, item)
            seen.add(curr[1])
        return res




        