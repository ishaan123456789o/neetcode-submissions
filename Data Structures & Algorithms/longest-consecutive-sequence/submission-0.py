class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        elements = set(nums)
        res = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                count = 1
                curr = num + 1
                while curr in elements:
                    count += 1
                    seen.add(curr)
                    curr += 1
                res = max(res, count)
        return res

        