'''
[1,1,2,8]
[48,24,6,1]
48, 24, 12,8

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        cur = 1
        for i in range(len(nums)):
            res[i] = cur
            cur *= nums[i]
        
        cur = 1
        for i in reversed(range(len(nums))):
            res[i] *= cur
            cur *= nums[i]
        
        return res

        