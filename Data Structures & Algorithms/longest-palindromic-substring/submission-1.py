class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        resStart = 0
        resEnd = 0
        for i in range(len(s)):
            currLen = 1
            l = i-1
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen += 2
                l -= 1
                r += 1
            if currLen > maxLen:
                amt = (currLen-1)//2
                maxLen = currLen
                resStart = i-amt
                resEnd = i+amt
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                currLen = 2
                l = i-1
                r = i+2
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    currLen += 2
                    l -= 1
                    r += 1
                if currLen > maxLen:
                    amt = (currLen-2)//2
                    maxLen = currLen
                    resStart = i-amt
                    resEnd = i+amt+1
        return s[resStart : resEnd+1]



        