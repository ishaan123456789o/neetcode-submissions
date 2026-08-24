class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))
        while pq:
            addBack = None
            curr = heapq.heappop(pq)
            if len(res) < 2:
                res += curr[1]
                if curr[0] + 1 != 0:
                    heapq.heappush(pq, (curr[0]+1, curr[1]))
            else:
                if res[-1] == curr[1] and res[-2] == curr[1]:
                    if not pq:
                        break
                    else:
                        addBack = curr
                        curr = heapq.heappop(pq)
                        res += curr[1]
                        if curr[0] + 1 != 0:
                            heapq.heappush(pq, (curr[0]+1, curr[1]))
                else:
                    res += curr[1]
                    if curr[0] + 1 != 0:
                        heapq.heappush(pq, (curr[0]+1, curr[1]))
            if addBack:
                heapq.heappush(pq, addBack)
        return res
            

        