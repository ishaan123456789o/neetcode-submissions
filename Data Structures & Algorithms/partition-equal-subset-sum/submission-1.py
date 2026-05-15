class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = int(total/2)
        memo = {}
        for i in range(len(nums)):
            memo[(0, i)] = True
        def dp(remaining, i):
            if i >= len(nums):
                return False
            if (remaining, i) not in memo:
                memo[(remaining, i)] = False
                if remaining - nums[i] >= 0:
                    memo[(remaining, i)] = memo[(remaining, i)] or dp(remaining-nums[i], i+1)
                memo[(remaining, i)] = memo[(remaining, i)] or dp(remaining, i+1)
                
            return memo[(remaining, i)]
        return dp(target, 0)
            
            
        