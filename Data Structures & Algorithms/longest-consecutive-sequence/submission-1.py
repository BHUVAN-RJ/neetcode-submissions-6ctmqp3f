class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #intutinton being is prev is not in set means -> start this is how we solve
        hset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hset:
                length = 1
                while num + length in hset:
                    length += 1
                longest = max(longest, length)

        return longest 
            
