class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] in seen:
                nums[i], nums[-1] = nums[-1], nums[i]
                nums.pop()
                length -= 1
            else:
                seen.add(nums[i])
                i += 1
        nums.sort()
        return len(nums)