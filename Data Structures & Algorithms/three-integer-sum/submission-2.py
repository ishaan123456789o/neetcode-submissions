class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if (i > 0 and nums[i] != nums[i-1]) or i == 0:
                target = -nums[i]
                l = i+1
                r = len(nums)-1
                while l < r:
                    if nums[l] + nums[r] == target:
                        res.append([nums[i], nums[l], nums[r]])
                    if nums[l] + nums[r] < target:
                        curr = nums[l]
                        while nums[l] == curr and l < len(nums):
                            l += 1
                    else:
                        curr = nums[r]
                        while nums[r] == curr and r >= 0:
                            r -= 1
        return res
        