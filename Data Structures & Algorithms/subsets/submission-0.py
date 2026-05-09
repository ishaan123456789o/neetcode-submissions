class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr, i):
            if i >= len(nums):
                res.append(curr)
                return
            backtrack(curr + [nums[i]], i+1)
            backtrack(curr, i+1)
        backtrack([], 0)
        return res

        