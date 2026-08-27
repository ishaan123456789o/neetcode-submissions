class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    start = mid
                    break
                else:
                    r = mid-1
            else:
                if target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    end = mid
                    break
                else:
                    l = mid+1
            else:
                if target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
        return [start,end]
