class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        cur = 1
        for i in range(len(nums)):
            res[i] *= cur
            cur *= nums[i]
        print(res)
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        
        return res

        
            
            # [1, 1, 2, 8]
            # [48,24,6,1]



        