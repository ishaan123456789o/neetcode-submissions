class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)
        res = r
        while l <= r:
            mid = (l+r)//2
            hour = 0
            i = 0
            while i < len(piles):
                if piles[i]%mid == 0:
                    hour += piles[i]/mid
                else:
                    hour += piles[i]//mid + 1
                i += 1
            if hour <= h:
                res = min(mid, res)
                r = mid - 1
            else:
                l = mid + 1
        return res