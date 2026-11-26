class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        copy = set(nums)
        res = 0
        for num in nums:
            if num - 1 in copy:
                continue
            count = 1
            while True:
                if num + 1 not in copy:
                    break
                count += 1
                num += 1
            res = max(count, res)
        return res
        