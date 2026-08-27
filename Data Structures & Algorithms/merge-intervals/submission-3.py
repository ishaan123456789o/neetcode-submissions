class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedByEndTime = sorted(intervals, key = lambda x: x[1])
        res = []
        for interval in sortedByEndTime:
            if not res:
                res.append(interval)
            else:
                if interval[0] > res[-1][1]:
                    res.append(interval)
                else:
                    currInterval = interval
                    addOn = None
                    while res and currInterval[0] <= res[-1][1]:
                        addOn = [min(res[-1][0], interval[0]), max(interval[1], res[-1][1])]
                        res.pop()
                        currInterval = addOn
                    res.append(addOn) 
        return res

        