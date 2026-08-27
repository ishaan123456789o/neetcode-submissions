class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tuple --> (node, the node we just came from)
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        q = deque()
        q.append((0, None))
        seen = set()
        seen.add(0)
        while q:
            for _ in range(len(q)):
                currentTuple = q.popleft()
                previousNode = currentTuple[1]
                currentNode = currentTuple[0]
                for node in adjList[currentNode]:
                    if node in seen and node != previousNode:
                        return False
                    elif node != previousNode:
                        q.append((node, currentNode))
                        seen.add(node)
        if len(seen) == n:
            return True
        return False
        
        