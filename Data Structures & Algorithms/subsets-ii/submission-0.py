class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(path, i, prev):
            if i >= len(nums):
                res.append(path)
                return
            if prev == "keep" or prev == None or (i > 0 and nums[i-1] != nums[i]):
                backtrack(path + [nums[i]], i + 1, "keep")
                backtrack(path, i+1, "skip")
            else:
                backtrack(path, i+1, "skip")
        backtrack([], 0, None)
        return res
            
        