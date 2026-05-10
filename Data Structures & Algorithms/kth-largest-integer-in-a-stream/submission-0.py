class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        for num in nums:
            heapq.heappush(self.pq, -num)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, -val)
        readd = []
        for i in range(self.k-1):
            curr = heapq.heappop(self.pq)
            readd.append(curr)
        res = heapq.heappop(self.pq)
        readd.append(res)
        for num in readd:
            heapq.heappush(self.pq, num)
        return -res
        
