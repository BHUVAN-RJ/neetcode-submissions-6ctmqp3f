class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for i in nums:
            if i - 1 in numsSet:
                continue
            cur = 1
            j = i
            while j + 1 in numsSet:
                j = j + 1
                cur += 1
            res = max(cur, res)
        return res

        