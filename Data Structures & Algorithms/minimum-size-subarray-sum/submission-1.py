'''
l = 2
r = 5
cursum = 9
res = 3
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        cursum = 0
        res = float('inf')
        while r < len(nums):
            cursum += nums[r]
            while cursum >= target:
                res = min(res, (r-l+1))
                cursum -= nums[l]
                l += 1
            r += 1
        return 0 if res == float('inf') else res

        