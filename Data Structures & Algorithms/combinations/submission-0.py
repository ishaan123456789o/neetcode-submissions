class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, path):
            if len(path) == k:
                res.append(path)
                return
            if i > n:
                return
            backtrack(i+1, path)
            backtrack(i+1, path + [i])
        backtrack(1, [])
        return res