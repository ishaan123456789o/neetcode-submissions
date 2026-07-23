class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[0, 0]] * len(nums) #element 0 of tuple represents with last house, element 1 represents w/o
        dp[-1] = [nums[-1], 0]
        for i in range(len(nums)-2, -1, -1):
            dp[i] = [nums[i], nums[i]]
            for j in range(i+2, len(nums)):
                dp[i][0] = max(dp[i][0], nums[i] + dp[j][0])
                dp[i][1] = max(dp[i][1], nums[i] + dp[j][1])
        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i][1])
            if i != 0:
                res = max(res, dp[i][0])
        return res
