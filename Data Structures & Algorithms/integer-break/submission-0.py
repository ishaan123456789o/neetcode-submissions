class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * n
        dp[-1] = 1
        for i in range(n-2, 0, -1):
            dp[i] = n-i
            for j in range(i+1, n):
                dp[i] = max(dp[i], (j-i) * dp[j])
        for i in range(1, n):
            dp[0] = max(dp[0], i*dp[i])
        return dp[0]

        