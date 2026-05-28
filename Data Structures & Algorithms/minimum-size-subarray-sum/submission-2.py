'''
l = 2
r = 5
cursum = 9
res = 3
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, 0
        cursum = 0
        while r < len(nums):
            cursum += nums[r]
            print(cursum)
            
            if cursum >= target:
                while cursum >= target:
                    cursum -= nums[l]
                    l += 1
            
                res = min(res, r-l+2)
            r += 1
        
        return res if res != float('inf') else 0

        