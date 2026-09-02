class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        if len(nums) > 1:
            r = len(nums)-1
        else:
            r = 0
        res = 0
        while l <= r:
            mid = l + (r-l//2)
            if nums[mid] == target:
                res = mid
                break
            if nums[mid] < target:
                if mid + 1 < len(nums):
                    if nums[mid+1] > target:
                        res = mid + 1
                        break
                else:
                    res = mid + 1
                    break
                l = mid + 1
            else:
                if mid - 1 >= 0:
                    if nums[mid-1] < target:
                        res = mid
                        break
                else:
                    res = mid
                    break
                r = mid - 1
        return res


        