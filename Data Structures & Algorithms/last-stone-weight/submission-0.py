class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
        while len(pq) > 1:
            curr1 = -heapq.heappop(pq)
            curr2 = -heapq.heappop(pq)
            if curr2 != curr1:
                if curr2 > curr1:
                    heapq.heappush(pq, -(curr2 - curr1))
                else:
                    heapq.heappush(pq, -(curr1 - curr2))
        if len(pq) == 0:
            return 0
        return -pq[0]