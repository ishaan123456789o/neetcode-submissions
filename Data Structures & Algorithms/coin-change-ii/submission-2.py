class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(remaining, i):
            if (remaining, i) not in memo:
                if remaining == 0:
                    return 1
                if remaining < 0 or i >= len(coins):
                    return 0
                memo[(remaining, i)] = dp(remaining - coins[i], i) + dp(remaining, i+1)
            return memo[(remaining, i)]
        return dp(amount, 0)
        