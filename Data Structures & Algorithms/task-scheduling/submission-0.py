import itertools

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        nums = Counter(tasks)
        counter = itertools.count()
        cooldown = {}
        pq = []
        for key in nums.keys():
            cooldown[key] = 0
            heapq.heappush(pq, (-nums[key], next(counter), key))
        res = 0
        while pq:
            addback = []
            while pq:
                curr = heapq.heappop(pq)
                if cooldown[curr[2]] == 0:
                    count = curr[0] + 1
                    if count != 0:
                        heapq.heappush(pq, (count, next(counter), curr[2]))
                        cooldown[curr[2]] = n+1
                    break
                else:
                    addback.append(curr)
            for tup in addback:
                heapq.heappush(pq, tup)
            res += 1
            for key in cooldown.keys():
                if cooldown[key] > 0:
                    cooldown[key] -= 1
        return res

        