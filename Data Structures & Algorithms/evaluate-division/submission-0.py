class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i in range(len(equations)):
            numerator = equations[i][0]
            denominator = equations[i][1]
            adjList[numerator].append((denominator, values[i]))
            adjList[denominator].append((numerator, 1/values[i]))
        res = [-1] * len(queries)
        for i in range(len(queries)):
            query = queries[i]
            q = deque()
            if query[0] in adjList:
                q.append((query[0], 1))
            seen = set()
            target = query[1]
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr[0] == target:
                        res[i] = curr[1]
                        break
                    seen.add(curr[0])
                    for next in adjList[curr[0]]:
                        if next[0] not in seen:
                            calc = 0
                            calc = curr[1] * next[1]
                            q.append((next[0], calc))
        return res




        