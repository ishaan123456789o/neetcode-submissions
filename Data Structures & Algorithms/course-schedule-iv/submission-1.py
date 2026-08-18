class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        for prereq in prerequisites:
            adjList[prereq[1]].append(prereq[0])
        res = [False] * len(queries)
        for i in range(len(queries)):
            query = queries[i]
            target = query[0]
            start = query[1]
            q = deque()
            if start in adjList:
                q.append(start)
            seen = set()
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr == target:
                        res[i] = True
                        break
                    seen.add(curr)
                    for next in adjList[curr]:
                        if next not in seen:
                            q.append(next)
        return res

        