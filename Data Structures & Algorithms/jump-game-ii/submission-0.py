class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            dp[i] = float('inf')
            for j in range(i+1, min(len(nums), i+1+nums[i])):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]
        