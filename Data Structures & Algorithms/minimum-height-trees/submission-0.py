class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        rootToHeight = defaultdict(list)
        for i in range(n):
            root = i
            seen = set()
            q = deque()
            height = 0
            q.append(i)
            seen.add(i)
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    for node in adjList[curr]:
                        if node not in seen:
                            q.append(node)
                            seen.add(node)
                height += 1
            rootToHeight[height].append(i)
        return rootToHeight[min(rootToHeight.keys())]
        

        