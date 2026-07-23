class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        prereqs = defaultdict(list)
        post = defaultdict(list)
        for edge in prerequisites:
            prereqs[edge[0]].append(edge[1])
            post[edge[1]].append(edge[0])
        q = deque()
        for i in range(numCourses):
            if len(prereqs[i]) == 0:
                q.append(i)
                taken.add(i)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for course in post[curr]:
                    prereqs[course].remove(curr)
                    if len(prereqs[course]) == 0:
                        taken.add(course)
                        q.append(course)
        return len(taken) == numCourses


        