class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pq = []
        for key in count.keys():
            heapq.heappush(pq, (-count[key], key))
        res = []
        for i in range(k):
            curr = heapq.heappop(pq)[1]
            res.append(curr)
        return res
        