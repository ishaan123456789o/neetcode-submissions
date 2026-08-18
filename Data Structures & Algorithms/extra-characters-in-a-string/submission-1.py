class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = {}
        dictionary = set(dictionary)
        memo[len(s)] = 0
        def dp(start):
            if start not in memo:
                memo[start] = len(s)-start
                for i in range(start+1, len(s)+1):
                    if s[start:i] in dictionary:
                        memo[start] = min(memo[start], dp(i))
                memo[start] = min(memo[start], 1+dp(start+1)) 
            return memo[start]
        return dp(0)
        