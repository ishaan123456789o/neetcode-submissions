class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if i + 2 < len(nums):
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
            else:
                dp[i] = max(nums[i], dp[i+1])
        return dp[0]
        