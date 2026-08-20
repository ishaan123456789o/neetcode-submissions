class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotateOnce():
            i = 1
            replaced = nums[0]
            save = nums[1]
            nums[1] = replaced
            replaced = save
            if i == len(nums)-1:
                i = 0
            else:
                i += 1
            while i != 1:
                save = nums[i]
                nums[i] = replaced
                replaced = save
                if i == len(nums)-1:
                    i = 0
                else:
                    i += 1
        if k % len(nums) != 0:
            for _ in range(k%len(nums)):
                rotateOnce()

        