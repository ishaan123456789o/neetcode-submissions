class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False
        def backtrack(start_index, remaining, seen):
            if remaining == 0: 
                if len(seen) == len(matchsticks):
                    return True
                else:
                    start_index = 0
                    remaining = target
            for i in range(start_index, len(matchsticks)):
                if i not in seen and matchsticks[i] <= remaining:
                    if backtrack(i+1, remaining - matchsticks[i], seen | {i}):
                        return True
            return False
        return backtrack(0, target, set())

            
        