class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for flight in flights:
            adjList[flight[0]].append((flight[2], flight[1]))
        frontier = []
        for item in adjList[src]:
            heapq.heappush(frontier, (item[0], 0, item[1]))
        res = -1
        minStops = {}
        while frontier:
            current = heapq.heappop(frontier)
            airport = current[2]
            currentStops = current[1]
            costSoFar = current[0]
            if airport == dst:
                res = costSoFar
                break
            else:
                if currentStops < k and (airport not in minStops or minStops[airport] > currentStops):
                    minStops[airport] = currentStops
                    for dest in adjList[airport]:
                        heapq.heappush(frontier, (costSoFar + dest[0], currentStops + 1, dest[1]))
        return res

                
        