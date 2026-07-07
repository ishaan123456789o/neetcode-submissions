class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if (r-l+1)-max(count.values()) > k:
                res = max(res, r-l)
                while (r-l+1)-max(count.values()) > k:
                    count[s[l]] -= 1
                    l += 1
        res = max(res, len(s)-l)
        return res

        