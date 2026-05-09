class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def backtrack(i, remaining):
            nonlocal res
            if i == len(nums)-1:
                if nums[i] == -remaining:
                    res += 1
                if nums[i] == remaining:
                    res += 1
                return
            if i >= len(nums):
                return
            backtrack(i+1, remaining - nums[i])
            backtrack(i+1, remaining + nums[i])
        backtrack(0, target)
        return res
        