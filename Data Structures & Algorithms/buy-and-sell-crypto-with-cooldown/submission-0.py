class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, bought):
            if i >= len(prices):
                    return 0
            if (i, bought) not in memo:
                if bought:
                    memo[(i, bought)] = prices[i] + dp(i+2, False)
                    for x in range(i+1, len(prices)):
                        memo[(i, bought)] = max(memo[(i, bought)], prices[x] + dp(x+2, False))
                else:
                    memo[(i, bought)] = dp(i+1, True) - prices[i]
                    for x in range(i+1, len(prices)):
                        memo[(i, bought)]= max(memo[(i, bought)], dp(x+1, True) - prices[x])
            return memo[(i, bought)]
        return max(0, dp(0, False))
            