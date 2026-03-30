class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        curProd = 1
        for i in range(len(nums)):
            res[i] = curProd
            curProd *= nums[i]
        
        curProd = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= curProd
            curProd *= nums[i]
        
        return res


        