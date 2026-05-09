class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = nums[:]
        post = nums[:]
        for i in range(len(nums)):
            if i > 0:
                pre[i] = pre[i] * pre[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                post[i] = post[i] * post[i+1]
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = post[i+1]
            elif i == len(nums)-1:
                result[i] = pre[i-1]
            else:
                result[i] = post[i+1] * pre[i-1]
        return result
        