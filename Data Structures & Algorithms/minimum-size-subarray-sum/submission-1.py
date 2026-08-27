class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum = [0] * (len(nums)+1)
        prefixSum[0] = 0
        prefixSum[1] = nums[0]
        for i in range(2, len(prefixSum)):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        l = 0
        res = 0
        for r in range(1, len(prefixSum)):
            while prefixSum[r] - prefixSum[l] >= target:
                if res == 0:
                    res = r-l
                else:
                    if res > (r-l):
                        res = r-l
                l += 1
        return res
                



        