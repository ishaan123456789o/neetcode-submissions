class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        frontier = []
        adjList = defaultdict(list)
        for time in times:
            adjList[time[0]].append((time[2], time[1]))
        for item in adjList[k]:
            heapq.heappush(frontier, item)
        seen = set()
        seen.add(k)
        times = {}
        times[k] = 0
        while len(seen) < n:
            curr = None
            while (not curr or curr[1] in seen) and frontier:
                curr = heapq.heappop(frontier)
            if not curr:
                break
            seen.add(curr[1])
            times[curr[1]] = curr[0]
            for edge in adjList[curr[1]]:
                heapq.heappush(frontier, (edge[0] + times[curr[1]], edge[1]))
        if len(seen) < n:
            return -1
        return max(times.values())


            
        
        