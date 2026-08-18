class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if len(s) % 2 == 0:
            if max(counts.values()) > (len(s)/2):
                return ""
        else:
            if max(counts.values()) > ((len(s)//2) + 1):
                return ""
        pq = []
        for letter in counts.keys():
            heapq.heappush(pq, (-counts[letter], letter))
        res = ""
        justAdded = None
        while len(res) < len(s):
            curr = heapq.heappop(pq)
            addback = None
            if curr[1] == justAdded:
                addback = curr
                curr = heapq.heappop(pq)
            justAdded = curr[1]
            res += curr[1]
            if curr[0] != 1:
                heapq.heappush(pq, (curr[0]+1, curr[1]))
            if addback:
                heapq.heappush(pq, addback)
        return res
        