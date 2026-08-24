class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        memo[0] = 1
        def dp(remaining):
            if remaining not in memo:
                memo[remaining] = 0
                for num in nums:
                    if num <= remaining:
                        memo[remaining] += dp(remaining-num)
            return memo[remaining]
        return dp(target)
            