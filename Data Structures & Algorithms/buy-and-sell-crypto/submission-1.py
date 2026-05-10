class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                l = i
                r = i
            elif prices[i] > prices[r]:
                r = i
                res = max(res, prices[r]-prices[l])
        return res

        