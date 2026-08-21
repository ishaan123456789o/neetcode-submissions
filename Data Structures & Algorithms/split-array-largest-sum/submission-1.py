class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        memo = {}
        def dp(i, remaining):
            if (i, remaining) not in memo:
                if remaining == 1:
                    sum = 0
                    for x in range(i, len(nums)):
                        sum += nums[x]
                    memo[(i, remaining)] = sum
                else:
                    x = i
                    memo[(i, remaining)] = float('inf')
                    sum = 0
                    while len(nums)-x >= remaining:
                        sum += nums[x]
                        memo[(i, remaining)] = min(memo[(i, remaining)], max(sum, dp(x+1, remaining-1)))
                        x += 1
            return memo[(i, remaining)] 
        return dp(0, k)
        