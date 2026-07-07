class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        res = 0
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    seen.add(curr)
                    for n in adjList[curr]:
                        if n not in seen:
                            q.append(n)
        for i in range(n):
            if i not in seen:
                res += 1
                bfs(i)
        return res
            
        