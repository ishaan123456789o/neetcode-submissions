class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        res = []
        def backtrack(path, curr):
            nonlocal res
            if curr >= len(digits):
                res.append(path)
                return
            for ch in letters[digits[curr]]:
                backtrack(path + ch, curr + 1)
        backtrack("", 0)
        return res
        