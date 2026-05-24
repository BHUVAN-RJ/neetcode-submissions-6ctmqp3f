class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            curnum = i
            if curnum - 1 in nums:
                continue
            curlen = 1
            while curnum + 1 in nums:
                curlen += 1
                curnum += 1
            res = max(curlen, res)
        return res
        