class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        postreqs = defaultdict(list)
        for pair in prerequisites:
            prereqs[pair[0]].append(pair[1])
            postreqs[pair[1]].append(pair[0])
        res = []
        seen = set()
        q = deque()
        for i in range(numCourses):
            if i not in prereqs or len(prereqs[i]) == 0:
                res.append(i)
                q.append(i)
                seen.add(i)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for course in postreqs[curr]:
                    prereqs[course].remove(curr)
                    if len(prereqs[course]) == 0 and course not in seen:
                        res.append(course)
                        q.append(course)
                        seen.add(course)
        if len(res) < numCourses:
            return []
        return res

        