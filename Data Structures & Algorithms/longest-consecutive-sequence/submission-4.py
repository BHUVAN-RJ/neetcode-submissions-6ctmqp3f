class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        length = 0
        for i in nums:
            if i - 1 in vals:
                continue
            cur = 1
            while i + 1 in vals:
                cur += 1
                i += 1
            length = max(cur, length)
        return length
            