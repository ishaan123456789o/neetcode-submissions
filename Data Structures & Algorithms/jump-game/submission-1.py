class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            for x in range(nums[i]+1):
                if i + x < len(nums) and dp[i + x] == True:
                    dp[i] = True
                    break
        return dp[0]
        