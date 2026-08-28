class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        '''if s[-1] == '1':
            return False
        memo = {}
        memo[len(s)-1] = True
        def dp(i):
            if i not in memo:
                memo[i] = False
                for x in range(i+minJump, min(i+maxJump+1, len(s))):
                    if s[x] == '0':
                        memo[i] = memo[i] or dp(x)
                    if memo[i] == True:
                        break
            return memo[i]
        return dp(0)'''

        if s[-1] == '1':
            return False
        dp = [False] * len(s)
        dp[-1] = True
        for i in range(len(s)-2, -1, -1):
            for j in range(i+minJump, min(i+maxJump+1, len(s))):
                if s[j] == '0' and dp[j]:
                    dp[i] = True
                    break
        return dp[0]
        