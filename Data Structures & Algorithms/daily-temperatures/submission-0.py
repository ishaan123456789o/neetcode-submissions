class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostck = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while monostck and temperatures[monostck[-1]] < temperatures[i]:
                curr = monostck.pop()
                res[curr] = i-curr
            monostck.append(i)
        return res

        