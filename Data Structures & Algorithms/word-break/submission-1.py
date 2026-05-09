class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * len(s)
        trues = []
        trues.append(len(s))
        for i in range(len(s)-1, -1, -1):
            for end in trues:
                if s[i:end] in words:
                    dp[i] = True
                    trues.append(i)
                    break
        return dp[0]


        