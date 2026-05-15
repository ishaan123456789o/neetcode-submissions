class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r-l+1)
            else:
                res = max(res, r-l)
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[r])
                l += 1
                seen.add(s[r])
        return res

        