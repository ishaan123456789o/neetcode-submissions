class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = 0
        for i in range(min(len(str1), len(str2))):
            if len(str1) % (i+1) == 0 and len(str2) % (i+1) == 0:
                if str1[:i+1] * (len(str1)//(i+1)) == str1 and str1[:i+1] * (len(str2)//(i+1)) == str2:
                    res = i+1
        return str1[:res]
        