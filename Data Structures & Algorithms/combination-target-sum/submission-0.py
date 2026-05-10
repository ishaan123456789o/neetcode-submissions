class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()
        def backtrack(curr, path, i):
            nonlocal res
            if curr == target:
                res.append(path)
                return
            if curr > target or i >= len(nums):
                return
            backtrack(curr + nums[i], path + [nums[i]], i)
            backtrack(curr, path, i+1)
        backtrack(0, [], 0)
        return res
        