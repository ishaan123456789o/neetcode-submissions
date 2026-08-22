class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums)-1
        answer = 0
        while l <= r:
            mid = l + (r-l)//2
            if mid > 0:
                if nums[mid-1] > nums[mid]:
                    answer = nums[mid]
                    break
            else:
                if nums[-1] > nums[mid]:
                    answer = nums[mid]
                    break
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return answer
            
        