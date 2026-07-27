class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = defaultdict(set)
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes[l].add(r)
                l -= 1
                r += 1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes[l].add(r)
                l -= 1
                r += 1
        res = []
        def backtrack(path, i):
            if i >= len(s):
                res.append(path)
                return
            for end in list(palindromes[i]):
                backtrack(path + [s[i:end+1]], end+1)
            return
        backtrack([], 0)
        return res
            


        