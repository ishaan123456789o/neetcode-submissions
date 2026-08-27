class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        firstIndex = {}
        lastIndex = {}
        for i in range(len(s)):
            if s[i] not in firstIndex:
                firstIndex[s[i]] = i
                lastIndex[s[i]] = i
            else:
                lastIndex[s[i]] = i
        res = []
        i = 0
        while i < len(s):
            seen = set()
            seen.add(s[i])
            currEndIndex = lastIndex[s[i]]
            j = i
            while i <= currEndIndex:
                if s[i] not in seen:
                    if currEndIndex < lastIndex[s[i]]:
                        currEndIndex = lastIndex[s[i]]
                    seen.add(s[i])
                i+=1
            res.append(currEndIndex-j+1)
        return res
        