class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        if len(nums) < 2:
            return len(nums)
        
        for num in nums:
            if num - 1 in nums:
                continue
            curlen = 1
            curnum = num
            while curnum + 1 in nums:
                curlen += 1
                curnum += 1
            res = max(res, curlen)
        
        return res


        