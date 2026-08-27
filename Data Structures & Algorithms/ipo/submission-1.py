class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq = []
        for i in range(len(profits)):
            heapq.heappush(pq, (-profits[i], capital[i]))
        currentCapital = w
        remaining = k
        while remaining and pq:
            curr = heapq.heappop(pq)
            neededCapital = curr[1]
            profit = curr[0]*-1
            addBack = []
            while neededCapital > currentCapital and pq:
                addBack.append(curr)
                curr = heapq.heappop(pq)
                neededCapital = curr[1]
                profit = curr[0]*-1
            if not pq and neededCapital > currentCapital:
                break
            currentCapital += profit
            remaining -= 1
            if remaining > 0:
                for pair in addBack:
                    heapq.heappush(pq, pair)
        return currentCapital

        