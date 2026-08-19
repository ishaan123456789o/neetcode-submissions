class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(1, len(strs[0])+1):
            curr = strs[0][:i]
            match = True
            for x in range(1, len(strs)):
                if strs[x][:i] != curr:
                    match = False
                    break
            if match:
                res = curr
            else:
                break
        return res
        