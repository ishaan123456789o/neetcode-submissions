class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = defaultdict(int)
        def dp(sI, tI):
            nonlocal memo
            if (sI, tI) not in memo:
                if tI == len(t):
                    return 1
                if sI >= len(s):
                    return 0
                memo[(sI, tI)] = 0
                if s[sI] == t[tI]:
                    memo[(sI, tI)] += dp(sI + 1, tI + 1)
                memo[(sI, tI)] += dp(sI + 1, tI)
            return memo[(sI, tI)]
        return dp(0, 0)