class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0
        def dp(remaining):
            if remaining not in memo:
                memo[remaining] = float('inf')
                for coin in coins:
                    if remaining - coin >= 0:
                        memo[remaining] = min(memo[remaining], 1 + dp(remaining-coin))
            return memo[remaining]
        res = dp(amount)
        if res == float('inf'):
            return -1
        return res
                    


        