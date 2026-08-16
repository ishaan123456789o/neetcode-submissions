class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pq = []
        res = []
        origIndex = {}
        for i in range(len(tasks)):
            origIndex[(tasks[i][0], tasks[i][1])] = i
        tasks = sorted(tasks, key=lambda task: task[0])
        time = 0
        index = 0
        while tasks[index][0] > time:
            time += 1
        while index < len(tasks) and tasks[index][0] <= time:
            heapq.heappush(pq, (tasks[index][1], origIndex[(tasks[index][0], tasks[index][1])]))
            index += 1
        while len(res) < len(tasks):
            if pq:
                curr = heapq.heappop(pq)
                res.append(curr[1])
                time += curr[0]
            else:
                time += 1
            while index < len(tasks) and tasks[index][0] <= time:
                heapq.heappush(pq, (tasks[index][1], origIndex[(tasks[index][0], tasks[index][1])]))
                index += 1
        return res



        