class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        seen = defaultdict(int)
        seen[0] = 1
        res = 0
        for num in prefixSum:
            if num-k in seen:
                res += seen[num-k]
            seen[num] += 1
        return res