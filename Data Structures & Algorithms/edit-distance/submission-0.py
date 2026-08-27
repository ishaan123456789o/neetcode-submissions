class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(index1, index2):
            if (index1, index2) not in memo:
                if index2 >= len(word2):
                    return len(word1) - index1
                if index1 >= len(word1):
                    return len(word2) - index2
                memo[(index1, index2)] = float('inf')
                if word1[index1] == word2[index2]:
                    memo[(index1, index2)] = min(memo[(index1, index2)], dp(index1+1, index2+1))
                else:
                    memo[(index1, index2)] = min(memo[(index1, index2)], 1 + dp(index1+1, index2+1)) # replace character
                    memo[(index1, index2)] = min(memo[(index1, index2)], 1 + dp(index1+1, index2)) # delete character
                    memo[(index1, index2)] = min(memo[(index1, index2)], 1 + dp(index1, index2+1))
            return memo[(index1, index2)]
        return dp(0, 0)
        