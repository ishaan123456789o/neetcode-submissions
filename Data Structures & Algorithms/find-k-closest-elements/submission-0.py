class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = 0
        lowestDiff = float('inf')
        for i in range(len(arr)):
            if abs(arr[i]-x) < lowestDiff:
                lowestDiff = abs(arr[i]-x)
                closest = i
            elif abs(arr[i]-x) == lowestDiff:
                if arr[closest] > arr[i]:
                    closest = i
        l = closest
        r = closest
        while r-l+1 < k:
            rightDiff = float('inf')
            leftDiff = float('inf')
            if r+1 < len(arr):
                rightDiff = abs(arr[r+1]-x)
            if l-1 >= 0:
                leftDiff = abs(arr[l-1]-x)
            if rightDiff == leftDiff or leftDiff < rightDiff:
                l -= 1
            else:
                r += 1
        return arr[l:r+1]

        