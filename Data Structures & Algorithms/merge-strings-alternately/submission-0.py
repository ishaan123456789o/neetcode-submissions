class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = 0
        i2 = 0
        res = []
        while i1 < len(word1) and i2 < len(word2):
            res.append(word1[i1])
            res.append(word2[i2])
            i1 += 1
            i2 += 1
        if i1 < len(word1):
            res.append(word1[i1:])
        elif i2 < len(word2):
            res.append(word2[i2:])
        return "".join(res)
        