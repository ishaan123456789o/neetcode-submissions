class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''dp = [0] * len(prices)
        for i in range(len(dp)-2, -1, -1):
            dp[i] = max(dp[i+1] + (prices[i+1]-prices[i]), dp[i+1])
        return dp[0]'''

        currentState = 0
        for i in range(len(prices)-2, -1, -1):
            currentState = max(currentState + (prices[i+1]-prices[i]), currentState)
        return currentState
        