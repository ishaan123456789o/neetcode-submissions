class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(startI, endI):
            if (startI, endI) not in memo:
                if startI == endI:
                    memo[(startI, endI)] = (piles[startI], 0)
                else:
                    person1 = 0
                    person2 = 0
                    takesFirst = dp(startI + 1 , endI)
                    takesLast = dp(startI, endI - 1)
                    if piles[startI] + takesFirst[1] > piles[endI] + takesLast[1]:
                        memo[(startI, endI)] = (piles[startI] + takesFirst[1], takesFirst[0])
                    else:
                        memo[(startI, endI)] = (piles[endI] + takesLast[1], takesLast[0])
            return memo[(startI, endI)]
        results = dp(0, len(piles)-1)
        if results[0] > results[1]:
            return True
        return False
        