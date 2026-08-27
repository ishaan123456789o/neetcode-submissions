class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        #tuple --> (currentPlayer, nextPlayer)
        prefixSum = [0] * len(piles)
        prefixSum[0] = piles[0]
        for i in range(1, len(piles)):
            prefixSum[i] = prefixSum[i-1] + piles[i]
        memo = {}
        def dp(i, M):
            if (i, M) not in memo:
                if i >= len(piles):
                    return (0, 0)
                memo[(i, M)] = (0, float('inf'))
                currentPrefSum = 0
                if i-1 >= 0:
                    currentPrefSum = prefixSum[i-1]
                for x in range(i, min(len(piles), i+(2*M))):
                    if (prefixSum[x]-currentPrefSum) + dp(x+1, max(M, x-(i-1)))[1] > memo[(i, M)][0]:
                        memo[(i, M)] = (prefixSum[x]-currentPrefSum + dp(x+1, max(M, x-(i-1)))[1], dp(x+1, max(M, x-(i-1)))[0])
            return memo[(i, M)]
        return dp(0, 1)[0]
        