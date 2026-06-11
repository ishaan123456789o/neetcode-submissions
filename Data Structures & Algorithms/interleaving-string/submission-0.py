class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if i == len(s1) and len(s2) != j:
                    return s2[j:] == s3[i+j:]
                if i != len(s1) and len(s2) == j:
                    return s1[i:] == s3[i+j:]
                if i == len(s1) and j == len(s2):
                    return True
                
                if s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                    memo[(i, j)] = dp(i+1, j) or dp(i, j+1)
                elif s1[i] == s3[i+j] and s2[j] != s3[i+j]:
                    memo[(i, j)] = dp(i+1, j)
                elif s1[i] != s3[i+j] and s2[j] == s3[i+j]:
                    memo[(i, j)] = dp(i, j+1)
                else:
                    memo[(i, j)] = False
            return memo[(i, j)]
        return dp(0, 0)
        