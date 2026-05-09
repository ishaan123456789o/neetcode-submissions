class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if len(s2) < length:
            return False
        l = 0
        s1map = Counter(s1)
        s2map = {}
        for r in range(len(s2)):
            if s2[r] in s2map:
                s2map[s2[r]] += 1
            else:
                s2map[s2[r]] = 1
            if r >= length-1:
                same = True
                for key in s1map.keys():
                    if key not in s2map or s2map[key] != s1map[key]:
                        same = False
                        break
                if same:
                    return True
                s2map[s2[l]] -= 1
                if s2map[s2[l]] == 0:
                    del s2map[s2[l]]
                l += 1
        return False


        