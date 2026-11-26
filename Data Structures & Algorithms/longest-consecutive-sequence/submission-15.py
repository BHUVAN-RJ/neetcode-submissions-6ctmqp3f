class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        copy = set(nums)
        res = 1
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
        