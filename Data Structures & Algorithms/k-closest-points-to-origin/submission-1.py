class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceFromOrigin(x, y):
            X = x**2
            Y = y**2
            combined = X + Y
            return math.sqrt(combined)
        pq = []
        res = []
        for point in points:
            dist = distanceFromOrigin(point[0], point[1])
            heapq.heappush(pq, (dist, point))
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
        