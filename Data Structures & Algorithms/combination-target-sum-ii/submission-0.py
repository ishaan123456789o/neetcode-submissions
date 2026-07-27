class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(path, total, i):
            if total == target:
                res.append(path)
                return
            if total > target or i >= len(candidates):
                return
            backtrack(path + [candidates[i]], total + candidates[i], i+1)
            curr = candidates[i]
            while i < len(candidates) and curr == candidates[i]:
                i += 1
            backtrack(path, total, i)
        backtrack([], 0, 0)
        return res


        