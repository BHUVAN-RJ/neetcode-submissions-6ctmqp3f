class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # you can get the start from looking is the prev is not in the array = start of seq
        nums = set(nums)
        res = 0
        for cur in nums:
            if cur - 1 not in nums:
                length = 1
                while cur + 1 in nums:
                    cur = cur + 1
                    length = length + 1
                
                res = max(length, res)

        return res
        