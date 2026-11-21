class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0 ,0
        cursum = 0
        maxsum = nums[0]
        while r < len(nums):
            cursum += nums[r]
            r += 1
            maxsum = max(cursum, maxsum)
            if cursum <= 0:
                l = r
                cursum = 0
        return maxsum
        