class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique = set()
        res = []
        def backtrack(path, seen):
            if len(path) == len(nums):
                if tuple(path) not in unique:
                    res.append(path)
                    unique.add(tuple(path))
                return
            for i in range(len(nums)):
                if i not in seen:
                    backtrack(path + [nums[i]], seen | {i})
        backtrack([], set())
        return res
                

        