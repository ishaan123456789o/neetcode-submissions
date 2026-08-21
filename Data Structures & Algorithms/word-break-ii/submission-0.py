class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        res = []
        def backtrack(i, path):
            if i >= len(s):
                res.append(path)
                return
            for x in range(i, len(s)+1):
                if s[i:x] in words:
                    if x == len(s):
                        backtrack(x, path + s[i:x])
                    else:
                        backtrack(x, path + s[i:x] + " ")
            return
        backtrack(0, "")
        return res


        